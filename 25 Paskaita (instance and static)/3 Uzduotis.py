
class TimeUtils:

    @staticmethod
    def time_to_seconds(time_string):
        d = time_string.split(":")
        return f"Time converted to seconds: {(int(d[0]) * 60 + int(d[1])) * 60 + int(d[2])}"

seconds = TimeUtils()
print(TimeUtils.time_to_seconds("4:58:26"))


