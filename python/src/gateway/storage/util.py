import pika, json


def upload(f, fs, channel, access):
	try:
		fid = fs.put(f)
	except Exception as err:
		return "Internal server error", 500

	
	message = {
		"video_fid": str(fid),
		"mp3_fid": None,
		"username": access["username"]
	}


	try:
		channel.basic_publish(
				exchange="",
				routing_key="video",
				body=json.dumps(message), #for converting message obj into a JSON string
				properties=pika.BasicProperties(
					delivery_mode=pika.spec.PERSITENT_DELIVERY_MODE
				),

			)
	except:
		fs.delete(fid)
		return "Internal Server error", 500

		