# data_533_group_project
Group Project for Data-533 - Building a golf companion python package / application

Our module structure does not follow the requirements in that each sub-package does not have 2 sub-modules because this was not necessary for our project (Khalad approved this). Instead, the golf_companion package has 2 sub-packages (track_score and pick_club) with the following modules (start_tracking.py and start_picking.py), respectively. In addition, there is another module under golf_companion called "start_game.py" that uses the 2 sub-packages to simulate a round of golf. There are also 


│  
└── golf_companion/  
    ├── __init__.py  
    ├── __player_class.py  
    ├── __course_class.py  
    ├── start_game.py  
    ├── pick_club/  
    │   ├──  __init__.py  
    │   └──  start_picking.py   
    ├── track_score/   
    │   ├──  __init__.py   
    │   └──  start_tracking.py   
    └── course_files/   
        ├── sunset_ranch.csv  
        ├── shadow_ridge.csv  
        └── okanagan_golf_club_bear.csv   


golf_companion/  
│  
├── __init__.py  
├── __player_class.py  
├── __course_class.py  
├── start_game.py  
│  
├── pick_club/  
│   ├── __init__.py  
│   └── start_picking.py  
│  
├── track_score/  
│   ├── __init__.py  
│   └── start_tracking.py  
│  
└── course_files/  
    ├── sunset_ranch.csv    
    ├── shadow_ridge.csv   
    └── okanagan_golf_club_bear.csv   

    


