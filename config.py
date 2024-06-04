import yaml

# 读取yml文件
# 返回配置项
def getConfig():
    with open('../application.yml', 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
    # 获取配置项的值
    return config
