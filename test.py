mport json
import os
from datetime import datetime

class BaseModel:
        def __init__(self, id, name, my_number, created_at=None, updated_at=None):
                    self.id = id
                            self.name = name
                                    self.my_number = my_number
                                            self.created_at = created_at or datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
                                                    self.updated_at = updated_at or datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

                                                        def to_dict(self):
                                                                    return {
                                                                                        '__class__': self.__class__.__name__,
                                                                                                    'id': self.id,
                                                                                                                'name': self.name,
                                                                                                                            'my_number': self.my_number,
                                                                                                                                        'created_at': self.created_at,
                                                                                                                                                    'updated_at': self.updated_at
                                                                                                                                                            }
                                                                        
                                                                        def save(self):
                                                                                    file_path = f'{self.__class__.__name__}.{self.id}.json'
                                                                                            with open(file_path, 'w') as f:
                                                                                                            data = {f'{self.__class__.__name__}.{self.id}': self.to_dict()}
                                                                                                                        f.write(json.dumps(data))

                                                                                                                            @classmethod
                                                                                                                                def load(cls, id):
                                                                                                                                            file_path = f'{cls.__name__}.{id}.json'
                                                                                                                                                    if not os.path.exists(file_path):
                                                                                                                                                                    raise FileNotFoundError(f'{file_path} does not exist.')

                                                                                                                                                                        with open(file_path, 'r') as f:
                                                                                                                                                                                        data = json.loads(f.read())
                                                                                                                                                                                                    class_name = data[f'{cls.__name__}.{id}']['__class__']
                                                                                                                                                                                                                if class_name != cls.__name__:
                                                                                                                                                                                                                                    raise TypeError(f'Expected {cls.__name__}, got {class_name}')

                                                                                                                                                                                                                                            obj = cls(**data[f'{cls.__name__}.{id}'])
                                                                                                                                                                                                                                                        return obj

