class Formatter:
    def format(self, workouts, template):
        raise NotImplementedError()


class CliFormatter(Formatter):
    generator = None

    def format(self, workouts, template):
        workout_list = []
        for e in workouts:
            workout_list.append("  - {} {}".format(e[0][0], e[1]))
        workout_list = "\n".join(workout_list)

        pre_text = "## {}".format(template['title'] if 'title' in template else "")
        post_text = "Do {} sets of each exercise".format(self.generator.sets)

        return pre_text + "\n\n" + workout_list + "\n\n" + post_text

