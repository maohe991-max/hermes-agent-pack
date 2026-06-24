#!/usr/bin/env python3
"""Validate frontmatter of all sub-agent markdown files in skills/sub-agents/"""

import os
import sys
import glob
import yaml

SUB_AGENTS_DIR = 'skills/sub-agents'


def validate_all():
    errors = 0
    all_files = sorted(glob.glob(os.path.join(SUB_AGENTS_DIR, '*.md')))

    for fpath in all_files:
        basename = os.path.basename(fpath)
        file_errors = []

        with open(fpath, encoding='utf-8') as f:
            content = f.read()

        # Extract YAML frontmatter (between --- markers)
        if not content.startswith('---'):
            file_errors.append('missing frontmatter (no leading ---)')
            data = {}
        else:
            parts = content.split('---', 2)
            if len(parts) < 3:
                file_errors.append('missing closing --- in frontmatter')
                data = {}
            else:
                yaml_text = parts[1]
                try:
                    data = yaml.safe_load(yaml_text)
                    if not isinstance(data, dict):
                        file_errors.append('frontmatter is not a dict')
                        data = {}
                    else:
                        # 1. name field exists
                        if 'name' not in data or not data['name']:
                            file_errors.append('missing name')

                        # 2. parent is agent-squad
                        parent = data.get('parent')
                        if parent != 'agent-squad':
                            file_errors.append(
                                f"parent must be 'agent-squad', got '{parent}'"
                            )

                        # 3. tags field exists and is an array
                        tags = data.get('tags')
                        if tags is None:
                            file_errors.append('missing tags')
                        elif not isinstance(tags, list):
                            file_errors.append('tags must be an array')

                        # 4. suggested_partners field exists
                        partners = data.get('suggested_partners')
                        if partners is None:
                            file_errors.append('missing suggested_partners')
                        elif not isinstance(partners, list):
                            file_errors.append(
                                'suggested_partners must be an array'
                            )
                        else:
                            # 5. Each suggested_partners reference must exist
                            for p in partners:
                                p_path = os.path.join(
                                    SUB_AGENTS_DIR, f"{p}.md"
                                )
                                if not os.path.exists(p_path):
                                    file_errors.append(
                                        f"suggested_partner '{p}' file not "
                                        f"found ({p}.md)"
                                    )

                except yaml.YAMLError as e:
                    file_errors.append(f'YAML parse error: {e}')
                    data = {}

        if file_errors:
            for err in file_errors:
                print(f"❌ {basename}: {err}")
            errors += 1
        else:
            tags_count = len(data.get('tags', []))
            partners_count = len(data.get('suggested_partners', []))
            print(
                f"✅ {basename}: valid "
                f"(tags: {tags_count}, partners: {partners_count})"
            )

    return errors


def main():
    errors = validate_all()
    if errors:
        print(f"\n❌ {errors} file(s) have errors!")
        sys.exit(1)
    else:
        print(f"\n🎉 All sub-agent files valid!")


if __name__ == '__main__':
    main()
