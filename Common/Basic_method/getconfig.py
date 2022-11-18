# -*- coding: utf-8 -*-

import os
import configparser


class Get_Config_Value:

    @staticmethod
    def get_file(file='config_file.ini'):
        file_dir = os.path.dirname(__file__)
        file = os.path.join(file_dir,file)
        return file

    @staticmethod
    def config_obj(file):
        file = Get_Config_Value.get_file(file)
        config = configparser.ConfigParser()
        config.read(file,encoding='utf-8')
        return config

    @staticmethod
    def get_values(file,*args):
        config_obj = Get_Config_Value.config_obj(file)
        if len(args) == 1:
            if config_obj.has_section(*args):
                print(config_obj.items(*args))
                return config_obj.items(*args)
            else:
                raise Exception('section节点未找到')
        elif len(args) == 2:
            if config_obj.has_option(*args):
                print(config_obj.items(*args))
                return config_obj.get(*args)
            else:
                raise Exception('options错误')
        else:
            raise Exception('传参错误')





if __name__ == '__main__':
    Get_Config_Value.get_values('config_file.ini','rc_mysql')