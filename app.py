from flask import Flask

app = Flask(__name__)


def sum_digits(number: str):
    sum_of_digits = 0
    for digit in number:
        sum_of_digits += int(digit)
    return sum_of_digits


@app.route('/sum-of-digits/<number>')
def sum_request(number: str):
    return sum_digits(number)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
