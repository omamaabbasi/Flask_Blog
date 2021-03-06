
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# @login_manager.user_loader
# def load_user(customer_id):
# 	return Tailor.query.get(int(customer_id))

# from __main__ import db

class User(db.Model, UserMixin):
	# __tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(20), unique=False, nullable=False )
	lastname = db.Column(db.String(20), unique=False, nullable=False )
	username = db.Column(db.String(20), unique=False, nullable=False )
	shop_name = db.Column(db.String(20), unique=False, nullable=True)
	number = db.Column(db.Integer, unique=False, nullable=False )
	address = db.Column(db.String(20), unique=False, nullable=False )
	imagefile = db.Column(db.String(20), nullable=True, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	user_type = db.Column(db.Integer, nullable=False, default = 0)
	# skill_type = db.Column(db.Integer, nullable=False , default = 0)
	is_embroidery = db.Column(db.Integer, default=0)
	is_partywear = db.Column(db.Integer, default=0)
	is_dailywear = db.Column(db.Integer, default=0)
	is_modestwear = db.Column(db.Integer, default=0)

	def __repr__(self):
		return f"User('{self.firstname}', '{self.lastname}', '{self.username}')"

	def is_active(self):
	    """True, as all users are active."""
	    return True

	def get_id(self):
	    """Return the email address to satisfy Flask-Login's requirements."""
	    return self.id

	def is_authenticated(self):
	    """Return True if the user is authenticated."""
	    return True

	def is_anonymous(self):
	    """False, as anonymous users aren't supported."""
	    return False







class Collection(db.Model):
	# __tablename__ = 'collection'
	id = db.Column(db.Integer, primary_key=True)
	# tname = db.Column(db.String(20), db.ForeignKey('User.username'),nullable=False )

	price = db.Column(db.String(20), nullable=False ) #stitchingprice
	title = db.Column(db.String(20), nullable=False )
	is_embroidery = db.Column(db.Integer, default=0)   
	is_partywear = db.Column(db.Integer, default=0)
	is_dailywear = db.Column(db.Integer, default=0)
	is_modestwear = db.Column(db.Integer, default=0)
	fabric = db.Column(db.Text, nullable=False )
	category = db.Column(db.Integer, nullable=False, default = 0)
	created_at = db.Column(db.DateTime, default=datetime.now().strftime("%B%d,%Y %I:%M%p"))
	updated_at =db.Column(db.DateTime,nullable=True)
	# date_posted = db.Column(db.DateTime,nullable=False,default= datetime(int(year), int(month), 1))
	# create_at_info = db.Column(datetime,now().strftime("%B%d,%Y %I:%M%p"))
	product_image = db.Column(db.String(20), nullable=False, default='default.jpg')
	description = db.Column(db.String(50), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User')#, backref=db.backref('collection', lazy=True))
	normal_quality_price = db.Column(db.Integer, default = 0)
	good_quality_price = db.Column(db.Integer, default = 0)
	best_quality_price = db.Column(db.Integer, default = 0)



	def __repr__(self):
		return f"Collection('{self.price}','{self.description}', '{self.title}')"


	def get_id(self):
	    """Return the email address to satisfy Flask-Login's requirements."""
	    return self.id

	def is_authenticated(self):
	    """Return True if the user is authenticated."""
	    return self.authenticated

# class Quality(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	dress_price = (db.Column(db.String(20), nullable=False ))#stuffprice
# 	total_price = (db.Column(db.String(20), nullable=False )) #totalpayable


# 	def __repr__(self):
# 		return f"Quality('{self.dress_price}','{self.total_price}')"


# 	def get_id(self):
# 	    return self.id


class Size(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(20), nullable=False ) #S M L
	category = db.Column(db.Integer, nullable=False, default = 0) # 0-Abaya 1-Hijab
	Length = db.Column(db.Float, nullable=True, default = 0)
	width = db.Column(db.Float, nullable=True, default = 0)
	Shoulder = db.Column(db.Float, nullable=True, default = 0)
	Armhole = db.Column(db.Float, nullable=True, default = 0)
	Sleeves = db.Column(db.Float, nullable=True, default = 0)
	Chest = db.Column(db.Float, nullable=True, default = 0)
	
	def __repr__(self):
		return f"Size('{self.title}','{self.category}')"


	def get_id(self):
	    return self.id

class Order(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	quantity = db.Column(db.Integer, nullable=False, default=1) 
	customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User')
	collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))
	collection = db.relationship('Collection')
	Length = db.Column(db.Float, nullable=True, default = 0)
	width = db.Column(db.Float, nullable=True, default = 0)
	Shoulder = db.Column(db.Float, nullable=True, default = 0)
	Armhole = db.Column(db.Float, nullable=True, default = 0)
	Sleeves = db.Column(db.Float, nullable=True, default = 0)
	Chest = db.Column(db.Float, nullable=True, default = 0)
	Is_Order_confirmed = db.Column(db.Boolean, default = False)
	Is_Order_rejected = db.Column(db.Boolean, default = False)
	# order_ready = db.Column(db.Boolean, default = False)
	normal = db.Column(db.Boolean, default = False)
	urgent = db.Column(db.Boolean, default = False)
	order_created_at = db.Column(db.DateTime, default=datetime.now().strftime("%B%d,%Y %I:%M%p"))
	total_amount = db.Column(db.Float, nullable=True, default = 0)

	def __repr__(self):
		return f"Order('{self.customer_id}','{self.collection_id}')"


	def get_id(self):
	    return self.id



class CustomSize(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User')
	name = db.Column(db.String(20), nullable=False ) # sister name
	relation = db.Column(db.String(20), nullable=False ) #sister, mother
	category = db.Column(db.Integer, nullable=False, default = 0) # 0-Abaya 1-Hijab
	Length = db.Column(db.Float, nullable=True, default = 0)
	width = db.Column(db.Float, nullable=True, default = 0)
	Shoulder = db.Column(db.Float, nullable=True, default = 0)
	Armhole = db.Column(db.Float, nullable=True, default = 0)
	Sleeves = db.Column(db.Float, nullable=True, default = 0)
	Chest = db.Column(db.Float, nullable=True, default = 0)
	# quantity = db.Column(db.Integer, nullable=False, default=1) 
	
	def __repr__(self):
		return f"Size('{self.user.username}', '{self.category}', '{self.relation}')"


	def get_id(self):
	    return self.id

# class OrderCompleted(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
# 	order = db.relationship('Order')
# 	customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
# 	user = db.relationship('User')


# 	def __repr__(self):
# 		return f"OrderCompleted('{self.order.order_id}')"

# 	def get_id(self):
# 	    return self.id