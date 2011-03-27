module Utils

	def Utils::CONSUMER_KEY
		"9qKm6RmzrSnTJH5AG09g"
	end
	
	def Utils::CONSUMER_SECRET
		"o7sPZgmVy7zxgwWMDqRstKn1Sp8UJX2dsJHfa6Mm7M"
	end
	
	def Utils::APP_NAME
		"Tweet Bash"
	end
	
	def Utils::APP_VERSION
		"0.3.0"
	end	

	def Utils::split_tweet(tweet)
		tweet = tweet.gsub("\n", " ")
		words = tweet.split(" ")
		lines = []
		lines << ""
		words.each do |word|
			if (lines[lines.size - 1].size + word.size + 1) < 76
					lines[lines.size - 1] += " " + word
			else
				lines[lines.size - 1] = add_symbol(lines[lines.size - 1], 80)
				lines << "  " + word
			end
		end
		lines[lines.size - 1] = add_symbol(lines[lines.size - 1], 80)
		return lines
	end
	
	def Utils::split_user_bio(bio)	
		words = bio.gsub("\n", " ")
		lines = []
		lines << ""
		words.each do |word|
			if (lines[lines.size - 1].size + word.size + 1) < 76
					lines[lines.size - 1] += " " + word
			else
				lines[lines.size - 1] = add_symbol(Terminal.colorize(lines[lines.size - 1], :yellow), 90)
				lines << " " + word
			end
		end
		lines[lines.size - 1] = add_symbol(Terminal.colorize(lines[lines.size - 1], :yellow), 90)
		return lines
	end

	def Utils::add_symbol(line, line_size)
		("| " + line + " "*(line_size - line.size - 3) + "|")
	end
end
	puts Utils.split_tweet("Hello world")
	puts Utils.split_user_bio("Hello world")
	puts Utils.CONSUMER_KEY
