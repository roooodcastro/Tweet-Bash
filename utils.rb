require "colors"

@CONSUMER_KEY = "9qKm6RmzrSnTJH5AG09g"
@CONSUMER_SECRET = "o7sPZgmVy7zxgwWMDqRstKn1Sp8UJX2dsJHfa6Mm7M"
@app_name = "Tweet Bash"
@app_version = "0.3.0"

def split_tweet(tweet)
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
	
def split_user_bio(bio)	
	words = bio.gsub("\n", " ")
	lines = []
	lines << ""
	words.each do |word|
		if (lines[lines.size - 1].size + word.size + 1) < 76
				lines[lines.size - 1] += " " + word
		else
			lines[lines.size - 1] = add_symbol(colorize(lines[lines.size - 1], :yellow), 90)
			lines << " " + word
		end
	end
	lines[lines.size - 1] = add_symbol(colorize(lines[lines.size - 1], :yellow), 90)
	return lines
end

def add_symbol(line, line_size)
	("| " + line + " "*(line_size - line.size - 3) + "|")
end
	
def colorize(text, color)
    Color.get_color(color) + text + Color.get_color(:normal)
end

puts split_tweet("Hello world")
puts split_user_bio("Hello world")
