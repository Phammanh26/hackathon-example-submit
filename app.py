from flask import Flask, request

import settings
from solver import ClassifyReviewSolver



review_solver = ClassifyReviewSolver()

app = Flask(__name__)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/review-solver/solve")
def solve():
    review_sentence = request.args.get('review_sentence')
    result = review_solver.solve(review_sentence)
    return {"result": result}


if __name__ == '__main__':
    app.run(host=settings.HOST, port=settings.PORT, debug=1)
