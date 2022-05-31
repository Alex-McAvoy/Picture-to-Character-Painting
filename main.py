import numpy as np
import PIL.Image as Image
import tkinter
import tkinter.filedialog as fd

"""
@Description: 根据图像生成字符画
@Date:2022/05/31 17:10:15
@Author: Alex_McAvoy
"""
class App(object):
    choose_path = ''  # 选择的文件
    generate_path = '' # 生成的文件

    """
    @Description: 生成应用窗口
    @Date:2022/05/31 17:12:23
    @Author: Alex_McAvoy
    @Params: NULL
    @Return: NULL
    """
    def createdWindow(self):
        window = tkinter.Tk()
        window.title("文本生成")
        # window.geometry("450x300")

        input_frame = tkinter.Frame(window)
        # 输入提示
        input_label = tkinter.Label(input_frame, text="请输入绘画所用字符(两到三个)：", justify=tkinter.LEFT)
        input_label.grid(row=1, column=0)
        # 输入
        input = tkinter.Entry(input_frame, bd=4)
        input.grid(row=1, column=1)
        input_frame.grid(row=1, column=0, padx=1, pady=1)
        

        choose_frame = tkinter.Frame(window)
        # 选择图片提示
        choose_label = tkinter.Label(choose_frame, text="请选择图片")
        choose_label.grid(row=1, column=0)

        # 输入字符提示
        tip_label = tkinter.Label(choose_frame, text="")
        tip_label.grid(row=2, column=0)

        # 选择图片按钮
        select = tkinter.Button(choose_frame, text="选择图片", command=lambda: self.openChooseWindow(choose_label))
        select.grid(row=3, column=1)

        # 开始转换按钮
        start = tkinter.Button(choose_frame, text="转换", command=lambda: self.generatePicture(input, tip_label))
        start.grid(row=3, column=7)

        choose_frame.grid(row=2, column=0, padx=10, pady=10)
        window.mainloop()

    """
    @Description: 打开选择文件窗口
    @Date:2022/05/31 17:58:30
    @Author: Alex_McAvoy
    @Params: choose_label 选择图片与转换框架
    @Return: NULL
    """
    def openChooseWindow(self,choose_label):
        choose_label["text"] = ""
        self.choose_path = fd.askopenfilename() # 选择的文件
        self.generate_path = self.choose_path.replace(self.choose_path.split("/")[-1].split(".")[-1],"txt") # 生成的文件
        choose_label["text"] = self.choose_path.split("/")[-1] # 选择后的提示信息
        print("---------------")
        print("选择的文件: " + self.choose_path)
        print("生成的文件: " + self.generate_path)

    """
    @Description: 生成字符画
    @Date:2022/05/31 18:32:32
    @Author: Alex_McAvoy
    @Params: input 输入内容, tip_label 输入字符提示
    @Return: NULL
    """
    def generatePicture(self,input,tip_label):
        str = list(input.get())
        str_len = len(str)
        if str_len<2 or str_len>3:
            tip_label["text"] = "请正确输入用来绘画的字符"
            return
        if str_len==2 or str_len==3:
            tip_label["text"] = "正在生成..."
        print("---------------")
        print("正在生成...")

        img = Image.open(self.choose_path)
        w, h = img.size
        w_s = int(w/20)  # 长宽缩小20倍
        h_s = int(h/20)  # 长宽缩小20倍
        img = img.resize((w_s, h_s),Image.ANTIALIAS)
        blank = (w_s - h_s)/2
        img = img.crop((0, -blank, w_s, w_s-blank))

        image = img.convert('L')
        image = np.array(image)

        # 两个字符
        if str_len == 2:
            with open(self.generate_path, 'w') as f:
                for i in range(int(len(image))):
                    for j in range(int(len(image[0]))):
                        if image[i][j] > 95:
                            f.write(str[0])
                        else:
                            f.write(str[1])
                    f.write("\n")
        
        
        # 三个字符
        if len(str) == 3:
            with open(self.generate_path, 'w') as f:
                for i in range(len(image)):
                    for j in range(len(image[0])):
                        st = int(image[i][j] / 85)
                        if st == 0:
                            f.write(str[0])
                        else:
                            if st == 1:
                                f.write(str[1])
                            else:
                                f.write(str[2])
                        # f.write(" ")
                    f.write("\n")

        tip_label["text"] = "生成成功！"
        print("---------------")
        print("生成成功！")

if __name__ == "__main__":
    app = App()
    app.createdWindow()
    
