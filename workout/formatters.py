from .exercises import S_ONE_PER_SIDE,S_SECONDS


class Formatter:
    def format(self, workouts, template):
        raise NotImplementedError()


class CliFormatter(Formatter):
    generator = None

    def format(self, workouts, template):
        workout_list = []
        for exercise, reps in workouts:
            name = exercise[0]
            sets = self.generator.sets
            reps = str(reps)
            if S_ONE_PER_SIDE in exercise[2]:
                name += " (one per side)"
            if S_SECONDS in exercise[2]:
                reps += "s"
            workout_list.append("  - {} {} x {}".format(name, reps, sets))
        workout_list = "\n".join(workout_list)

        pre_text = "{}".format(template['title'] if 'title' in template else "")

        return pre_text + "\n" + workout_list

