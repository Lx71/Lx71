#1.定义类： 初始化属性， 被烤和添加调料的方法， 显示用户信息的str
class SweetPotato():
    #始化属性
    def __init__(self):
        #烤制时间
        self.cook_time = 0
        #烤制状态
        self.cook_state = '生的'
        #添加调料
        self.cook_Season = []
    
    def cook(self， time):
        """烤地瓜方法"""
        #1.计算地瓜整体烤过的时间
        self.cook_time += time
        #2.通过整体考的时间判断烤的状态
        if 0 <= self.cook_time < 3:
            #生的
            self.cook_state = "生的"
        elif 3 <= self.cook_time < 5:
            #半生不熟
            self.cook_state = "半生不熟"
        elif 5 <= self.cook_time < 8:
            #熟了
            self.cook_state = "熟了"
        elif self.cook_time >= 8:
            #烤糊了
            self.cook_state = "烤糊了"
            
    def add_Season(self，season):
    	if season != '':
        	self.cook_Season。append(season)  
    def __str__(self):
        return f'烤制时间:{self.cook_time},\n烤制状态:{self.cook_state},\n添加的调料{self.cook_Season}。'
        
#创建对象并调用对应实例方法
digua1 = SweetPotato()
while True:
	digua1.cook(int(input("输入烤制时间:")))
	digua1.add_Season(input("输入添加调料:"))
	print(digua1)
	if digua1.cook_state == "熟了" or digua1.cook_state == '烤糊了':
		break
