import re
from typing import List, Union

class Token:
    def __init__(self, type_: str, value: str):
        self.type = type_
        self.value = value

class Lexer:
    def __init__(self):
        self.keywords = {
            'buzz': 'FUNCTION',
            'sting': 'PRINT',
            'nest': 'IF',
            'hive': 'WHILE',
            'honey': 'RETURN',
            'swarm': 'LIST',
            'drone': 'FOR',
            'queen': 'CLASS',
            'worker': 'VAR',
        }
        
    def tokenize(self, code: str) -> List[Token]:
        tokens = []
        current = ''
        i = 0
        
        while i < len(code):
            char = code[i]
            
            if char.isspace():
                if current:
                    tokens.append(self._create_token(current))
                    current = ''
                i += 1
                continue
                
            if char in '=+-*/<>(){}[];,':
                if current:
                    tokens.append(self._create_token(current))
                    current = ''
                tokens.append(Token('SYMBOL', char))
                i += 1
                continue
                
            if char == '"':
                if current:
                    tokens.append(self._create_token(current))
                    current = ''
                string = ''
                i += 1
                while i < len(code) and code[i] != '"':
                    string += code[i]
                    i += 1
                tokens.append(Token('STRING', string))
                i += 1
                continue
                
            current += char
            i += 1
            
        if current:
            tokens.append(self._create_token(current))
            
        return tokens
    
    def _create_token(self, value: str) -> Token:
        if value in self.keywords:
            return Token(self.keywords[value], value)
        if value.isdigit():
            return Token('NUMBER', value)
        return Token('IDENTIFIER', value)

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        
    def parse(self) -> List[dict]:
        statements = []
        while self.pos < len(self.tokens):
            stmt = self._parse_statement()
            if stmt:
                statements.append(stmt)
        return statements
    
    def _parse_statement(self) -> Union[dict, None]:
        if self.pos >= len(self.tokens):
            return None
            
        token = self.tokens[self.pos]
        
        if token.type == 'PRINT':
            return self._parse_print()
        elif token.type == 'VAR':
            return self._parse_variable()
        elif token.type == 'FUNCTION':
            return self._parse_function()
        elif token.type == 'IDENTIFIER':
            return self._parse_function_call()
        
        self.pos += 1
        return None
    
    def _parse_print(self) -> dict:
        self.pos += 1  # Skip 'sting'
        if self.pos < len(self.tokens):
            value = self.tokens[self.pos].value
            self.pos += 1
            return {'type': 'print', 'value': value}
        return None
    
    def _parse_variable(self) -> dict:
        self.pos += 1  # Skip 'worker'
        if self.pos + 2 < len(self.tokens):
            name = self.tokens[self.pos].value
            self.pos += 2  # Skip name and '='
            value = self.tokens[self.pos].value
            self.pos += 1
            return {'type': 'variable', 'name': name, 'value': value}
        return None
    
    def _parse_function(self) -> dict:
        self.pos += 1  # Skip 'buzz'
        if self.pos < len(self.tokens):
            name = self.tokens[self.pos].value
            self.pos += 1  # Skip name
            params = []
            body = []
            
            # Skip opening brace
            while self.pos < len(self.tokens) and self.tokens[self.pos].value != '{':
                self.pos += 1
            self.pos += 1
            
            # Parse body until closing brace
            while self.pos < len(self.tokens) and self.tokens[self.pos].value != '}':
                stmt = self._parse_statement()
                if stmt:
                    body.append(stmt)
            
            self.pos += 1  # Skip closing brace
            return {'type': 'function', 'name': name, 'params': params, 'body': body}
        return None
    
    def _parse_function_call(self) -> dict:
        name = self.tokens[self.pos].value
        self.pos += 1
        if self.pos < len(self.tokens) and self.tokens[self.pos].value == '(':
            self.pos += 1  # Skip (
            args = []
            self.pos += 1  # Skip )
            return {'type': 'call', 'name': name, 'args': args}
        return None

class Compiler:
    def compile(self, code: str) -> str:
        lexer = Lexer()
        tokens = lexer.tokenize(code)
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        return self._generate_python(ast)
    
    # Fix the _generate_python method in the Compiler class
    def _generate_python(self, ast: List[dict]) -> str:
        python_code = []
        
        for node in ast:
            if node['type'] == 'print':
                if node['value'].startswith('"'):
                    python_code.append(f'print({node["value"]})')
                else:
                    python_code.append(f'print({node["value"]})')
            elif node['type'] == 'variable':
                if node['value'].startswith('"'):
                    python_code.append(f'{node["name"]} = {node["value"]}')
                else:
                    python_code.append(f'{node["name"]} = "{node["value"]}"')
            elif node['type'] == 'function':
                params = ', '.join(node['params'])
                body_code = []
                for stmt in node['body']:
                    if stmt['type'] == 'print':
                        body_code.append(f'    print("{stmt["value"]}")')
                if not body_code:
                    body_code = ['    pass']
                python_code.append(f'def {node["name"]}({params}):\n' + '\n'.join(body_code))
            elif node['type'] == 'call':
                args = ', '.join(node['args'])
                python_code.append(f'{node["name"]}({args})')
                
        return '\n'.join(python_code)