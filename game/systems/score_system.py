class ScoreSystem:
    MAX_TIME = 120       
    MAX_WETNESS = 100 
    MAX_TOWELS = 15

    WEIGHT_TIME = 0.5
    WEIGHT_WETNESS = 0.3
    WEIGHT_TOWELS = 0.2

    @staticmethod
    def calculate(elapsed_time: float, wetness: float, towels_collected: int) -> int:
        t_score = max(0.0, 1 - elapsed_time / ScoreSystem.MAX_TIME) * 100
        w_score = max(0.0, 1 - wetness / ScoreSystem.MAX_WETNESS) * 100
        towel_score = (towels_collected / ScoreSystem.MAX_TOWELS) * 100

        score = (
            ScoreSystem.WEIGHT_TIME    * t_score +
            ScoreSystem.WEIGHT_WETNESS * w_score +
            ScoreSystem.WEIGHT_TOWELS  * towel_score
        )

        return round(score)