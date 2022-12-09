from os import getenv

API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5706111544").split()))
OWNER_ID = int(getenv("OWNER_ID", "5706111544")) #ur id
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Summ:summ@cluster0.cbhjhuj.mongodb.net/?retryWrites=true&w=majority") # an database 
BOT_TOKEN = getenv("BOT_TOKEN", "5848741580:AAG_yJZf_yrGZ26P2anaWpQJZF8Z2O_64Uw")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT") #optional
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAPxgzt71NqtZwvPDG95fCfq55DF28MfZDpoPaAjkAUU1lJ00yEBaOUfj4_sCLiMfzEm5xhj2kVpTBPstEnZY42PvO2ncKYspQi8HEgTGPYwNJcDesnBDG5feVGYIxrQtTv9fMTCRGLl4H0_gLcO3RgUL9SGa-Zv_u7SWFom0NdTk73W24mRxdKOWSyq3R7ppZ2P0yw9y__fYussUZlCn5URxzCrGTp0_c6EOLHj8fOchY2aqLYpa5xEOWcAt7_ALeo8TiT5Jxcy93qBLOZWfojWo8GBiaHePJM2QXb0p3wCDD8uELlrF2h68QFCSixUJmEuza9fkdvSQ6ggi7PpvLIgAAAAFUHFo4AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
