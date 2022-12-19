from django.http import HttpResponse

# Create your views here.
def index(request):
    line1 = '<h1 style="text-align:center">未来的吃鸡游戏</h1>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    line3 = '<hr>'
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Flmg.jj20.com%2Fup%2Fallimg%2F4k%2Fs%2F01%2F21092412092K1E-0-lp.jpg&refer=http%3A%2F%2Flmg.jj20.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1674043970&t=487a3f780883011ee5e1a303f7f8e423" width = 1500>'
    return HttpResponse(line1+line4+line3+line2)

def play(request):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp5.itc.cn%2Fq_70%2Fimages03%2F20210612%2F2864355cb943497583e5143c20debc54.png&refer=http%3A%2F%2Fp5.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1674044795&t=bd436acea80779ba317d9c9269b56344" width = 800>'
    line3 = '<a href="/">返回主页面</a>'
    return HttpResponse(line1+line3+line2)
