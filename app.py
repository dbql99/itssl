from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route("/solutionpic/solutionpic.html")
def solution() :
    return render_template("/solutionpic/solutionpic.html")

@app.route("/solutionmap/차량보안.html")
def solution1() :
    return render_template("/solutionmap/차량보안.html")

@app.route("/solutionmap/벡엔드보안.html")
def solution2() :
    return render_template("/solutionmap/벡엔드보안.html")

@app.route("/solutionmap/사이버보안관리체계.html")
def solution3() :
    return render_template("/solutionmap/사이버보안관리체계.html")

@app.route("/describe/개발단계.html")
def describe() :
    return render_template("/describe/개발단계.html")

@app.route("/describe/모니터링대응.html")
def describe2() :
    return render_template("/describe/모니터링대응.html")

@app.route("/describe/사이버공격.html")
def describe3() :
    return render_template("/describe/사이버공격.html")

@app.route("/describe/사이버보안성공.html")
def describe4() :
    return render_template("/describe/사이버보안성공.html")

@app.route("/describe/사이버보안위험.html")
def describe5() :
    return render_template("/describe/사이버보안위험.html")

@app.route("/describe/생산단계.html")
def describe12() :
    return render_template("/describe/생산단계.html")

@app.route("/describe/생산후단계.html")
def describe6() :
    return render_template("/describe/생산후단계.html")

@app.route("/describe/완화조치.html")
def describe7() :
    return render_template("/describe/완화조치.html")

@app.route("/describe/위험관리확인.html")
def describe8() :
    return render_template("/describe/위험관리확인.html")

@app.route("/describe/위험평가분석.html")
def describe9() :
    return render_template("/describe/위험평가분석.html")

@app.route("/describe/위험평가최신.html")
def describe10() :
    return render_template("/describe/위험평가최신.html")

@app.route("/describe/하위조직.html")
def describe11() :
    return render_template("/describe/하위조직.html")



@app.route("/checkrequire/개발단계.html")
def checkrequire() :
    return render_template("/checkrequire/개발단계.html")

@app.route("/checkrequire/모니터링대응.html")
def checkrequire2() :
    return render_template("/checkrequire/모니터링대응.html")

@app.route("/checkrequire/사이버공격.html")
def checkrequire3() :
    return render_template("/checkrequire/사이버공격.html")

@app.route("/checkrequire/사이버보안성공.html")
def checkrequire4() :
    return render_template("/checkrequire/사이버보안성공.html")

@app.route("/checkrequire/사이버보안위험.html")
def checkrequire5() :
    return render_template("/checkrequire/사이버보안위험.html")

@app.route("/checkrequire/생산단계.html")
def checkrequire6() :
    return render_template("/checkrequire/생산단계.html")

@app.route("/checkrequire/생산후단계.html")
def checkrequire7() :
    return render_template("/checkrequire/생산후단계.html")

@app.route("/checkrequire/완화조치.html")
def checkrequire8() :
    return render_template("/checkrequire/완화조치.html")

@app.route("/checkrequire/위험관리확인.html")
def checkrequire9() :
    return render_template("/checkrequire/위험관리확인.html")

@app.route("/checkrequire/위험평가분석.html")
def checkrequire10() :
    return render_template("/checkrequire/위험평가분석.html")

@app.route("/checkrequire/위험평가최신.html")
def checkrequire11() :
    return render_template("/checkrequire/위험평가최신.html")

@app.route("/checkrequire/하위조직.html")
def checkrequire12() :
    return render_template("/checkrequire/하위조직.html")


@app.route("/result/개발단계.html")
def result() :
    return render_template("/result/개발단계.html")


@app.route('/homepage.html')
def homepage():
    return render_template('/homepage.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
    
