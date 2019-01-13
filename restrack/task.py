class Task:
    def __init__(self, name, requirements, *args, **kwargs):
        self.name = name
        self.requirements = self.load_requirement(requirements)

    def load_requirement(selfs, req):
        raise NotImplementedError

    def summarize(self, info):
        """Return summary of the task, given a dict of items defined in requirements
        """
        raise NotImplementedError

    def diff(self, infoA, infoB):
        """
        Parameters
        ----------
        infoA : dict
            stats for one task
        infoB : dict
            stats for the other task
        Returns
        -------
            int : performance of infoA - infoB
        """
        raise NotImplementedError