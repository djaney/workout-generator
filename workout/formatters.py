class Formatter:
    def format(self, workouts, template):
        raise NotImplementedError()


class CliFormatter(Formatter):
    generator = None

    def format(self, workouts, template):
        workout_list = []
        for e in workouts:
            name = e[0][0]
            reps = e[1]
            sets = self.generator.sets
            workout_list.append("  - {} {} x {}".format(name, reps, sets))
        workout_list = "\n".join(workout_list)

        pre_text = "## {}".format(template['title'] if 'title' in template else "")
        post_text = "<exercise> <reps> x <sets>"

        return pre_text + "\n\n" + workout_list + "\n\n" + post_text

