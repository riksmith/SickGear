# Stubs for tornado_py3.template (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, ContextManager, Dict, Iterable, List, Optional, TextIO, Union

class _UnsetMarker: ...

def filter_whitespace(mode: str, text: str) -> str: ...

class Template:
    name: Any = ...
    autoescape: Any = ...
    namespace: Any = ...
    file: Any = ...
    code: Any = ...
    loader: Any = ...
    compiled: Any = ...
    def __init__(self, template_string: Union[str, bytes], name: str=..., loader: Optional[BaseLoader]=..., compress_whitespace: Union[bool, _UnsetMarker]=..., autoescape: Optional[Union[str, _UnsetMarker]]=..., whitespace: Optional[str]=...) -> None: ...
    def generate(self, **kwargs: Any) -> bytes: ...

class BaseLoader:
    autoescape: Any = ...
    namespace: Any = ...
    whitespace: Any = ...
    templates: Any = ...
    lock: Any = ...
    def __init__(self, autoescape: str=..., namespace: Optional[Dict[str, Any]]=..., whitespace: Optional[str]=...) -> None: ...
    def reset(self) -> None: ...
    def resolve_path(self, name: str, parent_path: Optional[str]=...) -> str: ...
    def load(self, name: str, parent_path: Optional[str]=...) -> Template: ...

class Loader(BaseLoader):
    root: Any = ...
    def __init__(self, root_directory: str, **kwargs: Any) -> None: ...
    def resolve_path(self, name: str, parent_path: Optional[str]=...) -> str: ...

class DictLoader(BaseLoader):
    dict: Any = ...
    def __init__(self, dict: Dict[str, str], **kwargs: Any) -> None: ...
    def resolve_path(self, name: str, parent_path: Optional[str]=...) -> str: ...

class _Node:
    def each_child(self) -> Iterable[_Node]: ...
    def generate(self, writer: _CodeWriter) -> None: ...
    def find_named_blocks(self, loader: Optional[BaseLoader], named_blocks: Dict[str, _NamedBlock]) -> None: ...

class _File(_Node):
    template: Any = ...
    body: Any = ...
    line: int = ...
    def __init__(self, template: Template, body: _ChunkList) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...
    def each_child(self) -> Iterable[_Node]: ...

class _ChunkList(_Node):
    chunks: Any = ...
    def __init__(self, chunks: List[_Node]) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...
    def each_child(self) -> Iterable[_Node]: ...

class _NamedBlock(_Node):
    name: Any = ...
    body: Any = ...
    template: Any = ...
    line: Any = ...
    def __init__(self, name: str, body: _Node, template: Template, line: int) -> None: ...
    def each_child(self) -> Iterable[_Node]: ...
    def generate(self, writer: _CodeWriter) -> None: ...
    def find_named_blocks(self, loader: Optional[BaseLoader], named_blocks: Dict[str, _NamedBlock]) -> None: ...

class _ExtendsBlock(_Node):
    name: Any = ...
    def __init__(self, name: str) -> None: ...

class _IncludeBlock(_Node):
    name: Any = ...
    template_name: Any = ...
    line: Any = ...
    def __init__(self, name: str, reader: _TemplateReader, line: int) -> None: ...
    def find_named_blocks(self, loader: Optional[BaseLoader], named_blocks: Dict[str, _NamedBlock]) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _ApplyBlock(_Node):
    method: Any = ...
    line: Any = ...
    body: Any = ...
    def __init__(self, method: str, line: int, body: _Node) -> None: ...
    def each_child(self) -> Iterable[_Node]: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _ControlBlock(_Node):
    statement: Any = ...
    line: Any = ...
    body: Any = ...
    def __init__(self, statement: str, line: int, body: _Node) -> None: ...
    def each_child(self) -> Iterable[_Node]: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _IntermediateControlBlock(_Node):
    statement: Any = ...
    line: Any = ...
    def __init__(self, statement: str, line: int) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _Statement(_Node):
    statement: Any = ...
    line: Any = ...
    def __init__(self, statement: str, line: int) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _Expression(_Node):
    expression: Any = ...
    line: Any = ...
    raw: Any = ...
    def __init__(self, expression: str, line: int, raw: bool=...) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class _Module(_Expression):
    def __init__(self, expression: str, line: int) -> None: ...

class _Text(_Node):
    value: Any = ...
    line: Any = ...
    whitespace: Any = ...
    def __init__(self, value: str, line: int, whitespace: str) -> None: ...
    def generate(self, writer: _CodeWriter) -> None: ...

class ParseError(Exception):
    message: Any = ...
    filename: Any = ...
    lineno: Any = ...
    def __init__(self, message: str, filename: Optional[str]=..., lineno: int=...) -> None: ...

class _CodeWriter:
    file: Any = ...
    named_blocks: Any = ...
    loader: Any = ...
    current_template: Any = ...
    apply_counter: int = ...
    include_stack: Any = ...
    def __init__(self, file: TextIO, named_blocks: Dict[str, _NamedBlock], loader: Optional[BaseLoader], current_template: Template) -> None: ...
    def indent_size(self) -> int: ...
    def indent(self) -> ContextManager: ...
    def include(self, template: Template, line: int) -> ContextManager: ...
    def write_line(self, line: str, line_number: int, indent: Optional[int]=...) -> None: ...

class _TemplateReader:
    name: Any = ...
    text: Any = ...
    whitespace: Any = ...
    line: int = ...
    pos: int = ...
    def __init__(self, name: str, text: str, whitespace: str) -> None: ...
    def find(self, needle: str, start: int=..., end: Optional[int]=...) -> int: ...
    def consume(self, count: Optional[int]=...) -> str: ...
    def remaining(self) -> int: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: Union[int, slice]) -> str: ...
    def raise_parse_error(self, msg: str) -> None: ...