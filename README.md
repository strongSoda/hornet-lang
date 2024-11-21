# Hornet Programming Language

Hornet is a bee-themed programming language that compiles to Python. It features intuitive syntax with apian-inspired keywords.

## Installation

```bash
git clone [your-repo]/hornet-lang
cd hornet-lang
pip install -e .
```

## Language Features

### Keywords
- `worker` - Variable declaration
- `sting` - Print statement
- `buzz` - Function definition
- `nest` - If statement
- `hive` - While loop
- `honey` - Return statement
- `swarm` - List
- `drone` - For loop
- `queen` - Class definition

### Example
```hornet
worker message = "Hello from Hornet!"
sting message

buzz greet() {
    sting "Buzz buzz!"
}

greet()
```

### Usage
```bash
hornet yourfile.hornet    # Compiles to executable
./yourfile               # Run the compiled program
```

## Technical Details

### Compiler Architecture
1. **Lexer**: Tokenizes source code into language tokens
2. **Parser**: Converts tokens into Abstract Syntax Tree (AST)
3. **Compiler**: Transforms AST into executable Python code

### Token Types
- Keywords (`FUNCTION`, `PRINT`, `IF`, etc.)
- Identifiers (variable/function names)
- Symbols (operators, brackets)
- Strings (text in quotes)
- Numbers (integer values)

### AST Node Types
- Print statements
- Variable declarations
- Function definitions
- Function calls

## Project Structure
```
hornet_lang/
├── bin/
│   └── hornet           # CLI executable
├── hornet_lang/
│   ├── __init__.py
│   └── compiler.py      # Core compiler implementation
├── setup.py             # Package configuration
└── examples/
    └── hello.hornet     # Example programs
```

## Development

### Adding New Features
1. Add keyword to `Lexer.keywords`
2. Implement parsing in `Parser._parse_statement`
3. Add code generation in `Compiler._generate_python`

### Running Tests
```bash
python -m pytest tests/
```

## Limitations
- Basic control flow only
- No operator precedence
- Limited error handling
- Single-file programs only

## License
MIT License

## Contributing
1. Fork repository
2. Create feature branch
3. Submit pull request