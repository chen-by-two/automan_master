# -*- coding: utf-8 -*-
import os
import json
import yaml

class ExtractYaml:

    def __init__(self, yamldir, yamlfile):
        self.yamldir = yamldir
        self.yamlfile = yamlfile

    @staticmethod
    def get_project_dir():
        '''
        获取项目路径
        :return:
        '''
        path = os.path.split(os.path.dirname(os.path.dirname(__file__)))[0]
        test_file_path = os.path.join(path, 'TestFile')
        return test_file_path

    def get_yaml_value(self):
        '''
        读yaml
        :return:
        '''
        test_file_path = ExtractYaml.get_project_dir()
        yaml_file = os.path.join(test_file_path, self.yamldir, self.yamlfile)
        print(f'yaml_file-----{yaml_file}')
        with open(yaml_file, 'r', encoding='utf-8') as f:
            env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
        return env_config



    def modify_yaml_value(self,dict,key,value):
        test_file_path = ExtractYaml.get_project_dir()
        yaml_file = os.path.join(test_file_path, self.yamldir, self.yamlfile)
        print(f'yaml_file-----{yaml_file}')
        env_config = self.get_yaml_value()
        env_config[dict][0][key] = value
        with open(yaml_file, 'w', encoding='utf-8') as f:
            yaml.dump(env_config, f)



if __name__ == '__main__':
    a = ExtractYaml('xuchao', 'demo.yaml').get_yaml_value()
    print(a)
