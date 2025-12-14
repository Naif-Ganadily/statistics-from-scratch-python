# Statistics from Scratch

**Building statistical methods from first principles in Python.**

Hi Yash,

This repository is where we'll implement core statistical concepts from the ground up. I'm preparing for my PhD qualifying exam and need to deeply understand these methods. You'll learn statistics fundamentals while also learning professional software engineering practices.

The dual goal: (1) understand statistics by implementing the math directly, and (2) learn how real engineering teams structure code, collaborate, and maintain quality. As a future physician doing AI research, you'll likely manage research engineers or collaborate with ML teams. Understanding their workflow helps you hire well, communicate effectively, and avoid common pitfalls that sink research labs.

## What "From Scratch" Means

We implement everything using only the most primitive operations.

### You CAN use:
- Raw Python: `sum()`, `len()`, loops, comprehensions
- `math` module: `math.sqrt()`, `math.log()`, `math.exp()`
- NumPy arrays as containers only:
  - Indexing: `arr[0]`, `arr[1:5]`
  - Sorting: `np.sort(arr)` 
  - Basic arithmetic: `arr + 5`, `arr * 2`, `arr1 + arr2`
  - Shape operations: `arr.shape`, `arr.reshape()`

### You CANNOT use (in implementations):
- `np.mean()`, `np.median()`, `np.var()`, `np.std()`
- `np.quantile()`, `np.percentile()`, `np.cov()`, `np.corrcoef()`
- `scipy.stats` anything
- `statistics` module
- Any function that does the statistics for you

### Exception: Tests
In test files, you can use NumPy/SciPy to validate your implementation is correct.

```python
def test_mean():
    data = np.array([1, 2, 3, 4, 5])
    assert np.isclose(my_mean(data), np.mean(data))  # OK in tests
```

## Why This Approach

1. You understand what these functions actually do
2. You can explain the algorithms in interviews or exams  
3. You recognize when standard implementations might fail
4. You build intuition for statistical properties

## Repository Structure

```
statsfs/
  descriptive/
    central_tendency.py    # mean, median, mode
    dispersion.py          # variance, std, range
    shape.py               # skewness, kurtosis
  probability/
    distributions.py       # pdf, cdf implementations
    sampling.py            # random sampling methods
  inference/
    hypothesis.py          # t-test, chi-square, etc.
    intervals.py           # confidence intervals
  models/
    regression.py          # linear regression
  utils/
    validation.py          # input checking
  experiments/
    descriptive.ipynb
    probability.ipynb
    inference.ipynb
    models.ipynb
      data/
    

tests/
  test_central_tendency.py
  test_dispersion.py
  ...

scripts/
  examples.py              # usage demonstrations

requirements.txt
.gitignore
README.md
```

## Setup

You need Python 3.8+, Git, and a GitHub account.

**Clone and navigate:**
```bash
git clone <repo-url>
cd stats-from-scratch
```

**Create virtual environment:**
```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Verify setup:**
```bash
pytest -v
```

**Deactivate when done:**
```bash
deactivate
```

## Workflow

**All tasks and goals are tracked in GitHub Issues.** Check the Issues tab to see what needs to be done.

I'll create issues for each statistical concept with:
- Mathematical definition
- Implementation requirements
- Test expectations
- Any gotchas or hints

### Steps for each task:

**1. Pick an issue**
Go to the Issues tab, find an open issue, and comment that you're working on it.

**2. Create branch**
```bash
git checkout main
git pull origin main
git checkout -b feature/implement-mean  # Match the issue topic
```

**3. Implement + test**
- Write the function in the appropriate module
- Write tests in `tests/`
- Run `pytest -v` until tests pass
- Commit your work:
```bash
git add .
git commit -m "Implement mean function (closes #5)"  # Reference issue number
```

**4. Push and open PR**
```bash
git push origin feature/implement-mean
```
Then open a Pull Request on GitHub. In the PR description, write "Closes #5" (or whatever the issue number is) so GitHub automatically links and closes the issue when merged.

**5. Review**
I'll review, you iterate on feedback, then we merge. The issue closes automatically.

### If you find issues in my code

Part of this learning process is practicing professional code review. If you find a bug, unclear documentation, or potential improvement:

**1. Open a new issue**
- Go to Issues tab, click "New Issue"
- Title: Short description (e.g., "Bug: variance function fails on single element array")
- Body: Include:
  - What the problem is
  - How to reproduce it (code example)
  - What you expected vs what happened
  - Suggested fix (optional)

**2. Reference related code**
Link to the specific file and line number. GitHub lets you click on line numbers to get a permanent link.

**3. Label appropriately**
Use labels like `bug`, `documentation`, `enhancement`, `question`

**4. If you want to fix it yourself**
- Comment on the issue saying you'll work on it
- Follow the same workflow: branch, fix, test, PR
- Reference the issue in your PR: "Fixes #12"

Example issue:
```
Title: Bug: mean() crashes on empty list

Description:
The mean function in statsfs/descriptive/central_tendency.py doesn't 
handle empty arrays properly.

Reproduction:
```python
from statsfs.descriptive.central_tendency import mean
data = []
result = mean(data)  # Crashes with IndexError
```

Expected: Should raise ValueError with clear message
Actual: IndexError: list index out of range

Suggested fix: Add input validation at start of function
```

This is how real engineering teams communicate. Practice it here.

## Testing

Run all tests:
```bash
pytest
```

Run with details:
```bash
pytest -v
```

Run specific file:
```bash
pytest tests/test_central_tendency.py
```

Check coverage:
```bash
pytest --cov=statsfs
```

## Learning Path

Start with descriptive statistics, then probability, then inference.

**Phase 1: Descriptive Statistics**
- Mean (arithmetic, geometric, harmonic)
- Median, mode
- Variance, standard deviation
- Quantiles, percentiles
- Covariance, correlation

**Phase 2: Probability**
- Normal distribution (pdf, cdf)
- Binomial, Poisson distributions  
- Random sampling methods
- Central limit theorem demonstrations

**Phase 3: Inference**
- Hypothesis testing (t-test, chi-square)
- Confidence intervals
- p-values and significance
- Bootstrap methods

**Phase 4: Models**
- Simple linear regression
- Multiple regression
- Evaluation metrics (R², MSE)

## Code Quality Expectations

- Write clear docstrings explaining what each function does
- Use descriptive variable names
- Add comments for non-obvious math steps
- Keep functions focused (one function, one task)
- Handle edge cases (empty arrays, invalid inputs)

Example:
```python
def mean(data):
    """
    Calculate arithmetic mean of a dataset.
    
    Parameters:
        data: array-like of numeric values
        
    Returns:
        float: arithmetic mean
        
    Raises:
        ValueError: if data is empty
    """
    if len(data) == 0:
        raise ValueError("Cannot calculate mean of empty array")
    
    total = sum(data)
    n = len(data)
    return total / n
```

## Implementation Notes

For each statistical function, you should:

1. Start with the mathematical definition
2. Break it into steps
3. Implement each step explicitly
4. Test against known examples
5. Validate against NumPy (in tests only)

Example for variance:
```python
# Mathematical definition: σ² = Σ(xi - μ)² / n

def variance(data):
    # Step 1: Calculate mean
    mu = mean(data)
    
    # Step 2: Calculate squared differences
    squared_diffs = [(x - mu)**2 for x in data]
    
    # Step 3: Average the squared differences
    return sum(squared_diffs) / len(data)
```

## Resources

Statistics:
- Casella & Berger, "Statistical Inference" (standard PhD text)
- Larry Wasserman, "All of Statistics"
- Khan Academy Statistics & Probability

Computational:
- Numerical Recipes (Press et al.)
- "Computational Statistics" by Geof H. Givens

Git workflow:
- Git branching: https://www.youtube.com/watch?v=GZbeL5AcTgw
- Pull requests: https://www.youtube.com/watch?v=bf7pCxj6mEg

## Notes

- `.venv` is git-ignored (won't be pushed to GitHub)
- Always activate your virtual environment before working
- Pull latest changes before creating new branches
- Write tests first if you want (TDD approach)
- If stuck, open an issue and tag me

### On using AI tools (ChatGPT, Claude, Copilot, etc.)

You can use AI to help when you're stuck, but try to minimize it. Here's why and how:

**Why limit AI use:**
- You're here to learn by struggling through problems
- Copy-pasting AI solutions means you won't retain the knowledge
- The point is building intuition, not just working code
- I need you to actually understand this stuff so you can explain it back to me

**When AI is acceptable:**
- Debugging syntax errors or understanding error messages
- Looking up NumPy array operations you're allowed to use
- Understanding mathematical notation from papers
- Getting unstuck after you've tried for 30+ minutes

**When you should NOT use AI:**
- Asking it to implement the full function for you
- Generating test cases without understanding them
- Copying algorithms without working through the math yourself

**Best practice:**
1. Try to solve it yourself first (really try, 30 minutes minimum)
2. If stuck, review the math from textbooks or notes
3. Still stuck? Ask me via GitHub issue
4. Last resort: use AI, but then rewrite the solution in your own words and make sure you understand every line

If you use AI help for any implementation, mention it in your PR description. No judgment, but it helps me know where to focus code review on understanding vs correctness.

Remember: struggling is part of learning. The confusion you feel right before understanding something is where real learning happens.

## Common Pitfalls

**Numerical stability:** Naive variance calculation can lose precision. We'll implement numerically stable versions.

**Edge cases:** Always test with empty arrays, single elements, negative numbers, very large/small numbers.

**Bessel's correction:** Sample variance uses n-1, population uses n. Implement both.

**Type handling:** Decide whether to work with lists or NumPy arrays. Document assumptions.

## Goal

By the end, you'll have:
- Deep understanding of statistical algorithms
- Portfolio of well-tested implementations  
- Experience with collaborative development
- Confidence implementing papers/textbook algorithms

This is active learning. You won't truly understand variance until you've debugged why your implementation gives slightly different results than NumPy's.

Let me know if you have questions. Open an issue or message me directly.
Good luck.

Naif
