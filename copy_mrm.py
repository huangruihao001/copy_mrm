# 参考网址：https://www.cnblogs.com/ssyfj/p/9051734.html
import os
import shutil

def copy_mrm(name):




    mrm_name = name + ".mrm"
    from_path = "./VR/vrlib/" + mrm_name
    to_path = "./date/VR/vrlib/" + mrm_name
    shutil.copyfile(from_path, to_path)

    from_path_jpg = "./VR/mod/" + name + ".jpg"
    to_path_jpg = "./date/VR/mod/" + name + ".jpg"
    shutil.copyfile(from_path_jpg, to_path_jpg)

    from_path_jpg_2d = "./VR/mod/" + name + "_2d.jpg"
    to_path_jpg_2d = "./date/VR/mod/" + name + "_2d.jpg"
    shutil.copyfile(from_path_jpg_2d, to_path_jpg_2d)

    from_path_mod = "./VR/mod/" + name + ".mod"
    to_path_mod = "./date/VR/mod/" + name + ".mod"
    shutil.copyfile(from_path_mod, to_path_mod)







if __name__ == '__main__':

    # 判断路径是否存在
    try:
        os.makedirs("./date/VR/vrlib")
        os.makedirs("./date/VR/mod")
    except:
        pass

    f = open("mrm.txt")             # 返回一个文件对象
    line = f.readline()             # 调用文件的 readline()方法

    while line:
        name = line.replace("\n", "")
        try:
            copy_mrm(name)
        except:
            print("复制错误：" + name)
        line = f.readline()
    print("复制完成，结果保存在date文件夹中！\n")
    input("按回车键继续……")