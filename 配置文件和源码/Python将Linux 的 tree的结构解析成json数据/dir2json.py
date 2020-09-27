import json, os

path = "c:/test"
def list_dir(path, res):
    for i in os.listdir(path):
        temp_dir = os.path.join(path, i)
        if os.path.isdir(temp_dir):
            temp = {"dirname": i, 'child_dirs': [], 'files': []}
            res['child_dirs'].append(list_dir(temp_dir, temp))
        else:
            res['files'].append(i)
    return res


def get_config_dirs(path):
    res = {'base_dirname': path, 'child_dirs': [], 'files': []}  # 定义总的模板格式
    return list_dir(path, res)


if __name__ == '__main__':
    print(json.dumps(get_config_dirs(path=path)))  # 转json而已