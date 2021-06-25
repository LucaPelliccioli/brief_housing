#from app.base import Base, Session, engine
#from app.prix_med import Prix_Median
from pandas.core.frame import DataFrame
from base import Base, Session, engine
from prix_med import Prix_Median


#{1,	"<1H OCEAN"}
#2	"INLAND"
#3	"NEAR OCEAN"
#4	"ISLAND"
#0	"NEAR BAY"

Base.metadata.create_all(engine)

def read_long_lat_proxi():
    """
        SELECT * FROM prix_median
        --> extraire tous les biens de BD
        Return: list de bien 
    """
    session = Session()
    # data est une liste de tuple
    long_lat_proxi_data = session.query(Prix_Median.longitude,
                         Prix_Median.latitude,
                         Prix_Median.ocean_proximity_str,
                         Prix_Median.ocean_proximity).all()
    session.close()
    list_long_lat = DataFrame(long_lat_proxi_data)
    list_long_lat = list_long_lat.drop_duplicates()
    return list_long_lat
 


def ajout_nv_bien(nvbien: Prix_Median):
    session = Session()
    #verifie la table 'prix_median exist dans DB ou non
    #si non, on va la créer 
    if not (engine.has_table('prix_median')):
         engine.create_all()
    
    session.add(nvbien)
    session.commit()
    session.close()
    print('ajout a termine !')
    
    

#long_lat_proxim = read_long_lat_proxi()

#print(long_lat_proxim )
nvbien = Prix_Median(-122.23, 37.88, 45 , 980, 350, 322, 126, 8, 0 , 0, "NEAR BAY")

ajout_nv_bien(nvbien)