# SuperDuper Project

A comprehensive learning journey combining Python programming fundamentals, SQL database operations, and data visualization. This project serves as a hands-on tutorial for developers learning to integrate multiple technologies including Python, SQL, data analysis, and web frameworks. 

Born out of the beginners frustration of finding a spot with easily understandable examples as well as links to additional resources and cheatsheets.

## Project Overview

This project is designed to demonstrate:
- Python programming fundamentals (strings, integers, functions, conditionals)
- SQL database operations and queries
- Data visualization with matplotlib and pandas
- Integration of multiple tools in a cohesive project
- Best practices for project organization and documentation

## Learning Path

The project follows a structured learning approach:

1. **Python Fundamentals** - Basic concepts and syntax
2. **SQL Basics** - Database queries and data manipulation
3. **Data Integration** - Combining Python and SQL
4. **Data Visualization** - Creating charts and graphs
5. **Project Organization** - Professional development practices

## Project Structure

```
SuperDuper/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── SuperDuper.ipynb         # Main Jupyter notebook
├── src/                     # Source code
│   ├── python_examples/     # Python learning examples
│   ├── sql_queries/         # SQL scripts and queries
│   └── data_analysis/       # Data analysis scripts
├── data/                    # Database and data files
│   └── cyberchase.db       # Sample SQLite database
├── notebooks/               # Additional Jupyter notebooks
├── scripts/                 # Utility scripts
└── docs/                   # Additional documentation
```

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd /Users/esmahoney/SuperDuper
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

5. **Open the main notebook:**
   - Navigate to `SuperDuper.ipynb` in your browser
   - Start exploring the learning modules!

## Sample Database

The project includes a SQLite database (`data/cyberchase.db`) containing information about Cyberchase TV episodes with the following schema:

- `id` - Unique identifier for each episode
- `season` - Season number
- `episode_in_season` - Episode number within the season
- `title` - Episode title
- `topic` - Educational topic covered
- `air_date` - Original air date (YYYY-MM-DD)
- `production_code` - PBS internal production ID

## Learning Modules

### Python Fundamentals
- String manipulation and formatting
- Integer operations and calculations
- Function definitions and parameters
- Conditional statements and logic
- Boolean expressions and comparisons

### SQL Operations
- Basic SELECT queries
- Data filtering and sorting
- Aggregations and grouping
- Database connections from Python

### Data Visualization
- Bar charts with matplotlib
- Data processing with pandas
- Statistical analysis and insights

## Getting Started

1. Start with the main `SuperDuper.ipynb` notebook
2. Follow the step-by-step learning modules
3. Experiment with the provided code examples
4. Try modifying queries and visualizations
5. Build your own analysis using the sample data

## Tools and Technologies

- **Python**: Core programming language
- **SQLite**: Database for storing and querying data
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Creating static visualizations
- **Jupyter**: Interactive development environment
- **Git**: Version control (optional)

## Future Enhancements

Potential additions to expand the project:
- Integration with external APIs
- Web interface using Gradio or Streamlit
- Additional visualization libraries (Seaborn, Plotly)
- Machine learning components
- Advanced SQL operations
- Deployment to cloud platforms

## Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to:
- Report issues or bugs
- Suggest additional learning modules
- Contribute example code
- Improve documentation

## License

This project is for educational purposes. Feel free to use and modify for your learning journey.

## 🙏 Acknowledgments

- Inspired by Harvard's CS50 Introduction to Programming with Python and SQL
- Cyberchase database used for educational examples
- Various online resources and tutorials mentioned in the notebook

---

**Happy Learning!**
