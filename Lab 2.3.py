


from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return "Hello World!"

#@app.route('/page1')
#def page1():
    #return "Если вы это читаете, \n\t вы что-то знаете :)"

if __name__=='__main__':
    app.run(debug=True)

print('=========================================================')

def modify_cubic(old_func):
    def new_cubic(arg):
        print('Вычисляем куб от ', arg)
        return old_func(arg)
    return new_cubic

@modify_cubic

def cubic(arg):
    return arg*arg*arg

for i in range (0,10):
    print(cubic(i))


#@app.route('/page1')
#def page1():
    #return "Если вы это читаете, \n\t вы что-то знаете :)"

#if __name__=='__main__':
    #app.run(debug=True)