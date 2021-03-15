import kivymd
import PIL
import random
from kivy.uix.videoplayer import VideoPlayer
import webbrowser
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition
from kivymd.uix.imagelist import SmartTileWithLabel
import webbrowser as wb
screen_helper = """
#: import Loader kivy.loader.Loader
#: import NoTransition kivy.uix.screenmanager.NoTransition
ScreenManager:
	MenuScreen:
	profilescreentwo:
	profilescreenthree:
	profilescreenfour:
	profilescreenfive:
	profilescreensix:
	profilescreenseven:
	subscreenone:						
	subscreentwo:	
	subscreenthree:
	subscreenfour:
	subscreenfive:
	subscreensix:
		
<MenuScreen>:
	name: 'menu'
	NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'              
                    MDToolbar:
        		        title: 'Text Material'
        		        type: 'top'
			            left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
			            elevation:10
                    BoxLayout :
                        orientation: 'vertical'                
                        ScrollView:
			                GridLayout:
				                cols: 1
				                
				                spacing: root.height/3
				                size_hint_y: None
				                height:self.minimum_height			            
			            
								MDList:
									ThreeLineAvatarIconListItem:
										text:"What is Cyber Saftey"
										font_style: 'H6'
										secondary_text:'cyber saftey refers to the safe and responsible'
										tertiary_text:"threat to aneone else's information"
										on_release:
											root.manager.current="profile2"
											root.manager.transition.direction = "up"
										IconLeftWidget:
											icon:'information-variant'		
									ThreeLineAvatarIconListItem:
										text:"Safley Browsing The Web"
										font_style: 'H6'
										secondary_text:'These days working on web has become inevitable'
										on_release:
											root.manager.current="profile3"
											root.manager.transition.direction = "up"											
										IconLeftWidget:
											icon:'database'
									ThreeLineAvatarIconListItem:
										text:"Confidentiality Of Information"
										font_style: 'H6'
										secondary_text:'Internet is a public platform,mostly.'
										on_release:
											root.manager.current="profile4"
											root.manager.transition.direction = "up"											
										IconLeftWidget:
											icon: 'code-brackets'
									ThreeLineAvatarIconListItem:
										text:"Cybercrime"
										font_style: 'H6'
										secondary_text:'Any criminal offence that is facilitated by,or involves'
										on_release:
											root.manager.current="profile5"
											root.manager.transition.direction = "up"											
										IconLeftWidget:
											icon:'code-parentheses'
									ThreeLineAvatarIconListItem:
										text:"Computer Forensics"
										font_style: 'H6'
										secondary_text:'Digital forensics or computer forensics refers '
										on_release:
											root.manager.current="profile6"
											root.manager.transition.direction = "up"											
										IconLeftWidget:
											icon:'code-braces'
									ThreeLineAvatarIconListItem:
										text:"Cyber Law And IT Act"
										font_style: 'H6'
										secondary_text:'Cyberlaw is a generic term which refers to all'
										on_release:
											root.manager.current="profile7"
											root.manager.transition.direction = "up"											
										IconLeftWidget:
											icon:'database'
        MDNavigationDrawer:
		    id:nav_drawer
		    BoxLayout:
		    	orientation:'vertical'
		    	
		    	padding:10
		    	spacing: 5
		    	AnchorLayout:
		    		anchor_x: 'left'
		    		
			    	AsyncImage:
			            source: "https://docs.google.com/drawings/d/e/2PACX-1vQ69SliAdrAkj2ydQ3c0Isdcy6TRs-dmLUDTizE02t87qnVOdIgMMZWJu8BpMh6ScR1U3toeV7Ziffq/pub?w=960&h=720"
			    BoxLayout:
			        orientation :'vertical'
			        size_hint_y:None
			        MDLabel:
			        	text: 'Next Level Tech'
			        	font_style: 'Overline'
			        	font_size: 40
			        	size_hint_y: None
			        	bold: True
			        	pos_hint:{'center_x':0.6,'center_y':10}
			        	font_colour: "blue"
				    MDList:
				    	OneLineIconListItem:
				    		text: 'Bookmarks'
				    		IconLeftWidget:
				            	icon: 'bookmark'
				    	OneLineIconListItem:
				    		text: 'settings'
				    		IconLeftWidget:
				            	icon: 'tools'
				    	OneLineIconListItem:
				    		text: 'About Us'
				    		IconLeftWidget:
				            	icon: 'information'
<profilescreentwo>:
	name: 'profile2'
	NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
	    			MDToolbar:
					    title: 'Introduction'
					    left_action_items: [["arrow-left",lambda x:  root.ch_sc()]]
					BoxLayout:
                    	orientation: 'vertical'
						ScrollView:
							GridLayout:
								cols: 1
								height: self.minimum_height
								size_hint_y: None
								MyTile:
									on_press: print('')
									AsyncImage:
										
										source:'https://docs.google.com/drawings/d/e/2PACX-1vSyu4XUZdUSfeXvURyD7c2ut0fiUoIF0AgSrKUTr815mNrorv9FyIs81Fc23D-KKBX6PLYQ6AxpKnEG/pub?w=1440&h=1080'
								MyTile:
									on_press: print('')
									AsyncImage:
										source:'https://docs.google.com/drawings/d/e/2PACX-1vSiUC9rHn8lpmggNfifeacBI1d1O8Ve3C7FzVjR-wLVy09PqBZ6DbBmrl6x6MmyXi2V3cp6qS0G-KBk/pub?w=1440&h=1080'
										
										
								
									
												
<profilescreenthree>:
	name: 'profile3'
	NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
	    			MDToolbar:
					    title: 'introduction'
					    left_action_items: [["arrow-left",lambda x:  root.ch_sc()]]
					BoxLayout:
                    	orientation: 'vertical'
						ScrollView:
							GridLayout:
								cols: 1
								height: self.minimum_height
								size_hint_y: None
									
<profilescreenfour>:
	name: 'profile4'
	NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
	    			MDToolbar:
					    title: 'introduction'
					    left_action_items: [["arrow-left",lambda x:  root.ch_sc()]]
					BoxLayout:
                    	orientation: 'vertical'
						ScrollView:
							GridLayout:
								cols: 1
								height: self.minimum_height
								size_hint_y: None
<profilescreenfive>:
	name: 'profile5'
	NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
	    			MDToolbar:
					    title: 'introduction'
					    left_action_items: [["arrow-left",lambda x:  root.ch_sc()]]
					BoxLayout:
                    	orientation: 'vertical'
						ScrollView:
							GridLayout:
								padding:25
								cols: 1
								height: self.minimum_height
								size_hint_y: None
								MDCard:
									elevation:7
									pos_hint: {'center_x': .5, 'center_y': .5}				
									size_hint: None,None
									size: root.width-50,(root.height/3)
									
								MDCard:
									elevation:7
									pos_hint: {'center_x': .5, 'center_y': .5}				
									size_hint: None,None
									size: root.width-50,(root.height/3)
								MDCard:
									elevation:7
									pos_hint: {'center_x': .5, 'center_y': .5}				
									size_hint: None,None
									size: root.width-50,(root.height/3)
									AsyncImage:
										source:'https://docs.google.com/drawings/d/e/2PACX-1vSiUC9rHn8lpmggNfifeacBI1d1O8Ve3C7FzVjR-wLVy09PqBZ6DbBmrl6x6MmyXi2V3cp6qS0G-KBk/pub?w=1440&h=1080'
								
<profilescreensix>:
	name: 'profile6'
	NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
	    			MDToolbar:
					    title: 'introduction'
					    left_action_items: [["arrow-left",lambda x:  root.ch_sc()]]
					BoxLayout:
                    	orientation: 'vertical'
						ScrollView:
							GridLayout:
								cols: 1
								height: self.minimum_height
								size_hint_y: None

<profilescreenseven>:
	name: 'profile7'
	NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
	    			MDToolbar:
					    title: 'introduction'
					    left_action_items: [["arrow-left",lambda x:  root.ch_sc()]]
					BoxLayout:
                    	orientation: 'vertical'
						ScrollView:
							GridLayout:
								cols: 1
								height: self.minimum_height
								size_hint_y: None


<MyTile@SmartTileWithLabel>
	image:'link'
    size_hint_y: None
    height: "240dp"
    box_color:0,0,0,0
"""
class MenuScreen(Screen):
	def set_sc(self):
	    MDApp.get_running_app().root.current = "profile"
	    MDApp.get_running_app().root.transition.direction="up"
	def set_screen(self):
		MDApp.get_running_app().root.current = "profile1"
		MDApp.get_running_app().root.transition = NoTransition(duration=0.001)	    
class profilescreentwo(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"      
class profilescreenthree(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class profilescreenfour(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class profilescreenfive(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"  	
class profilescreensix(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class profilescreenseven(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class subscreenone(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class subscreentwo(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class subscreenthree(Screen):  	
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class subscreenfour(Screen):  	
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class subscreenfive(Screen):  	
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class subscreensix(Screen):  	
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"	
class DemoApp(MDApp):  
    def build(self):
    	l=['Red', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Orange', 'DeepOrange',]
    	self.theme_cls.primary_palette = random.choice(l)
    	screen=Builder.load_string(screen_helper)
    	return screen
if __name__ == "__main__":
	DemoApp().run() 
