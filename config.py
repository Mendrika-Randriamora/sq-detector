# App configuration
APP_NAME = "Sq Detector"
APP_HOST = "0.0.0.0"
APP_PORT = 5050
UPLOAD_DIR = "static/uploads"

DB_NAME = "db.sqlite"

#=========================================

# Configuration for detection
# For Canny edges
LOW_THRESH = 50
RATIO = 3.0

# Minimum area accepted
MIN_AREA_ACCEPTED = 200

# For count rectangle in all outlines
MIN_DEG = 70
MAX_DEG = 110

MIN_RAT = 0.5
MAX_RAT = 1.5
