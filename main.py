import flet as ft
from flet import *
from checkbox import CustomCheckBox


def main(page: ft.Page):
    BG= '#041955'
    FWG='#224399'
    FG='#3c5a5d'
    PB= '#d8e08d'
    
    
    cercle= Stack(
    controls=[
      Container(
        width=100,
        height=100,
        border_radius=50,
        bgcolor='white12'
        ),
      Container(
                  gradient=SweepGradient(
                      center=alignment.center,
                      start_angle=0.0,
                      end_angle=3,
                      stops=[0.5,0.5],
                  colors=['#00000000', BG],
                  ),
                  width=100,
                  height=100,
                  border_radius=50,
                  content=Row(alignment='center',
                      controls=[
                        Container(padding=padding.all(5),
                          bgcolor=BG,
                          width=70,height=70,
                          border_radius=50,
                          content=Container(bgcolor=FG,
                            height=80,width=80,
                            border_radius=40,
                          content=CircleAvatar(opacity=0.8,
                foreground_image_url="ecommerce/assets/karl.jpg"
            )
                          )
                          )
                      ],
                  ),
              ),
      
    ]
  )
    
    
    
    def masque(e): #fonction qui masque notre UI
        page_2.controls[0].width= 120
        page_2.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right)
        page_2.controls[0].border_radius = border_radius.only(
            bottom_left=20, top_left=25, top_right=0, bottom_right=0
        )
        page_2.update()
        
    def restaure(e): #fonction qui permet d'afficher notre UI en clicquant sur l'icone
        page_2.controls[0].width= 250
        page_2.controls[0].border_radius = border_radius.all(20)
        page_2.controls[0].scale = transform.Scale(
            1, alignment=alignment.center_right)
        page_2.update()
    
    
    
    creer_commandes_view = Container(
        content= Container(
            on_click= lambda _: page.go('/'),
            height=40, width=40,
            content=Text('x')
        )
    )    
    
    
            
        
        
        
    #liste des éléments à afficher dans les commandes du jour
    commandes = Column(
        height=200,
        scroll= 'auto',
        # controls=[
           
        # ]
    )
    
    
    for i in range(10):
        commandes.controls.append(
             Container(
                height=50,
                width=400,
                bgcolor=FWG,
                border_radius=16,
                padding=padding.only(left=15, top=15),
                content=CustomCheckBox(
                    color=FWG,
                    label=f'Commande {i+1}', 
                    selection_fill=FWG, 
                    size=25, 
                    font_size=20,
                    stroke_width=2),
            )
        )
    
    categories_card= Row(
        scroll= 'auto'
    )
    categories= ['légumes', 'Fruits', 'produits', 'Viandes', 'poisson', 'boisson']
    for i, category in enumerate (categories):
        categories_card.controls.append(
            Container(
                border_radius= 10,
                bgcolor=FWG, 
                height=70,
                width=120,
                padding=8,
                content=Column(
                    controls=[
                        Text("En Stock"),
                        Text(category),
                        Container(
                            width=70,
                            height=5,
                            bgcolor=FG,
                            border_radius=10,
                            padding=padding.only(right=i*15),
                            content= Container(
                                bgcolor=PB,)),
                    ]
                )
                
            )
        )
    contenu_premiere_page = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(on_click= lambda e: masque(e),
                            content=Icon(
                                icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED),
                            ]
                        )
                    ]
                ),
                Container(height=20),#espacement avec les cards
                Text(
                    value="Bienvenue sur notre Market Place !"
                ),
                Text(
                    value="CATEGORIES"
                ),
                Container(
                    padding=padding.only(top=10, bottom=20 ),
                    content= categories_card
                ),
                Container(height=5),
                Text(
                    "Commandes du jour"
                ),
                Stack(#permet de faire un scroll sur plusieurs élements
                    controls=[
                        commandes,
                        FloatingActionButton(bottom=2, right=20 ,icon=icons.ADD, on_click= lambda _: page.go('/ajouter_commandes'))
                    ]
                )
            ]
            
        )
    )
    page_1 = Container(
        width=250,
        height=600,
        bgcolor= BG,
        border_radius=35,
        padding=padding.only(
        top=50, left=20,
        right=20, bottom=5
                ),
        content= Column(
            controls=[
                Row(alignment='end',
                   controls=[
                       Container(
                    border_radius=16,padding=padding.only(left=5, top=1),
                    height=30,width=30,border=border.all(color=PB,width=1),
                    on_click= lambda _: restaure('e'),
                    content=Text('<')
                       )
                   ] 
                ),
                Container(
                    height=20
                ),
                cercle,
                Text('Karl\nDavid', size=14, weight='bold'),
                Container(
                    height=20
                ),
                Row(
                    controls=[
                        Icon(icons.FAVORITE_BORDER_SHARP, color='white60'),
                        Text('favoris', size=15, weight=FontWeight.W_300, color='white', font_family='poppins'),
                    ]
                ),
                Container(
                    height=5
                ),
                Row(
                    controls=[
                        Icon(icons.CARD_TRAVEL, color='white60'),
                        Text('Particulier', size=15, weight=FontWeight.W_300, color='white', font_family='poppins'),
                    ]
                ),
                Container(
                    height=5
                ),
                Row(
                    controls=[
                        Icon(icons.CALCULATE_OUTLINED, color='white60'),
                        Text('Transactions', size=15, weight=FontWeight.W_300, color='white', font_family='poppins'),
                    ]
                ),
            ]
            
        )
    )
    page_2= Row(alignment='end',#propriété permetant d'aligné l'UI vers la droite lors du clic
        controls=[
            Container(
                width=250,
                height=600,
                bgcolor= BG,
                border_radius=35,
                animate=animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve="decelerate"),
                padding=padding.only(
                    top=50, left=20,
                    right=20, bottom=5
                ),
                content=Column(
                    controls=[
                        contenu_premiere_page
                    ]
                )
            )
        ]
    )
    
    container = Container(
    width=500,
    height=605,
    bgcolor= BG,
    border_radius=35, 
    content=Stack(
        controls=[
            page_1,
            page_2
        ]
    )
    )
    
    pages = {
        '/': View(
                  "/",
                  [
                   container   
                  ],  
            ),
        '/ajouter_commandes': View(
                            "/ajouter_commandes",
                            [
                                creer_commandes_view
                            ],
        )
    }
    
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
        
    
    
    
    # page.add(container)

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir='assets')
