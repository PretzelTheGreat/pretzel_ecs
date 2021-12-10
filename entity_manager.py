from uuid import uuid4 as U4


class EntityManager:
    """
    EntityManager() manages entities within a program. It is intended to be a
    static class, with the class brought in by importing it and accessing it directly.

    ...

    Attributes
    ----------
    tracked_entities : dict
        the dictionary that contains all the tracked entities with a dictionary containing
        all the attached components.

    Methods
    -------
    create_entity(data=None)
        Creates a new entity. Can be initialized empty or including data

    get_entity_data(entity_id)
        Retrieves data stored for the entity_id given

    attach_data(entity_id, data)
        Attaches new data to entity_id and stores it

    get_entities_with_data(data_comp)
        Searches all entities to get the ones with the supplied data components    

    """

    tracked_entities = {"top_entity": {}}

    @classmethod
    def create_entity(cls, data=None):
        """Creates a new entity to be tracked, and attaches any supplied data.

        If the argument 'data' is not passed in, a new entity id is given (given as a uuid)

        Parameters
        ----------
        data : dict, tuple, optional
            the data that the new entity will be initalized (default is None)
            if the data is given in a dict, the entity data will be set to the dictionary
            supplied
            or if the data is given as a tuple, it will create a new dict with the first entry
            in the tuple as the key and the second as the value
        """

        new_id = U4()

        if data != None and type(data) == tuple:
            cls.tracked_entities[new_id] = {data[0]: data[1]}

        elif data != None and type(data) == dict:
            cls.tracked_entities[new_id] = data

        else:
            cls.tracked_entities[new_id] = {}

        return new_id

    @classmethod
    def get_entity_data(cls, entity_id):
        """Gets the given entity's data that is being tracked.

        Parameters
        ----------
        entity_id : str
            the entity id to be looked up.
        """

        if entity_id in cls.tracked_entities.keys():
            return cls.tracked_entities[entity_id]

    @classmethod
    def attach_data(cls, entity_id, data):
        """Attaches new data to an existing entity

        Parameters
        ----------
        entity_id : str
            the entity id to attach the data to
        data : dict, list, tuple
            the data to be attached. the data must be in one of the following formats:
                tuple - (Name of Component [best if it is the name of the class], Object)
                dict - {Name of component: Object, (etc)}
                list - [list of tuple formats above]
        """

        if entity_id in cls.tracked_entities.keys():
            if type(data) == tuple:
                cls.tracked_entities[entity_id][data[0]] = data[1]
            elif type(data) == dict:
                for class_name, obj in data.items():
                    cls.tracked_entities[entity_id][class_name] = obj
            elif type(data) == list:
                for item in data:
                    cls.tracked_entities[entity_id][item[0]] = item[1]

    @classmethod
    def get_entities_with_data(cls, data_comp):
        """Returns entities with the supplied components
        Parameters
        ----------
        data_comp : list
            must be a list containing the components to be matched against
        """

        return [x for x in cls.tracked_entities.keys() if len(set(data_comp).intersection(cls.tracked_entities[x].keys())) == len(data_comp)]
