from uuid import uuid4 as U4


class EntityManager:
    tracked_entities = {"master_entity": {}}

    @classmethod
    def create_entity(cls, data=None):
        """Creates a new entity. Can be initialized empty or including data"""
        new_id = U4()

        if data != None:
            cls.tracked_entities[new_id] = {data[0]: data[1]}
            return new_id

        else:
            cls.tracked_entities[new_id] = {}
            return new_id

    @classmethod
    def get_entity_data(cls, entity_id):
        if entity_id in cls.tracked_entities:
            return cls.tracked_entities[entity_id]

    @classmethod
    def attach_data(cls, entity_id, data):
        """data must be in format (Name (Easiest if Classname), Object)"""
        if entity_id in cls.tracked_entities:
            cls.tracked_entities[entity_id][data[0]] = data[1]

    @classmethod
    def get_entities_with_data(cls, data_comp):
        return [x for x in cls.tracked_entities.keys() if len(set(data_comp).intersection(cls.tracked_entities[x].keys())) == len(data_comp)]
