# -*- coding: UTF-8 -*-
'''
Author: Linzjian666
Date: 2024-06-05 16:37:09
LastEditors: Linzjian666
LastEditTime: 2024-06-05 17:36:04
'''
import yaml

def read_profile(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        profile = yaml.safe_load(f)
    return profile

def write_profile(output_file, profile):
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(profile, f, sort_keys=False, allow_unicode=True)

def dedup_rules(rules):
    unique_rules = []
    deduped_rules = []
    for rule in rules:
        rule_key = ','.join(rule.split(',')[:2])
        if rule_key not in unique_rules:
            deduped_rules.append(rule)
            unique_rules.append(rule_key)
    return deduped_rules

def process_path(path):
    if "'" or '"' in path:
        path = path.replace("'", '').replace('"', '')
    return path

if __name__ == "__main__":
    input_file = process_path(input('请输入配置文件路径: '))
    output_file = process_path(input('请输入输出文件路径: '))
    profile = read_profile(input_file)
    rules = profile.get('rules', [])
    deduped_rules = dedup_rules(rules)
    profile['rules'] = deduped_rules
    write_profile(output_file, profile)
