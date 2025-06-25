"""A simple Flask app to square a number."""

from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

def square_number(number: float) -> float:
    """Returns the square of the given number."""
    return number ** 2

HTML_TEMPLATE = """
<form method="POST">
  Number: <input name="number" type="number" step="any">
  <input type="submit" value="Calculate">
</form>
{% if result is not none %}
  <p>Result: {{ result }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    """Handles form input and displays the squared result."""
    result = None
    if request.method == "POST":
        try:
            number = float(request.form["number"])
            result = square_number(number)
        except (ValueError, TypeError):
            result = "Invalid input!"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Cloud Run uses PORT=8080, local default is 5000
    app.run(debug=True, host="0.0.0.0", port=port)

