from django.db import models
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dacite import from_dict



@dataclass_json
@dataclass
class MsGraph():
    name: str
    id: str
    # file: Drive

@dataclass_json
@dataclass
class File(MsGraph):
    url: str

@dataclass_json
@dataclass
class Folder(MsGraph):
    folder_name: str
    
@dataclass
class A:
    x: str
    y: int


@dataclass
class B:
    a: A


data = {
    'a': {
        'x': 'test',
        'y': 1,
    }
}

result = from_dict(data_class=B, data=data)

assert result == B(a=A(x='test', y=1))