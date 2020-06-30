from food import Chicken
import brexit

chicken = Chicken()

if (brexit.referendum_result
    and brexit.referendum_result["leave"] > 50):
    raise ImportError
