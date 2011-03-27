module Terminal

	def Terminal::colorize(text, color)
		colors = {
		    :normal => "\033[m",
		    :reset => "\033[0;37;00m",
		    :black => "\033[0;30m",
		    :red => "\033[0;31m",
		    :green => "\033[0;32m",
		    :yellow => "\033[0;33m",
		    :blue => "\033[0;34m",
		    :violet => "\033[0;35m",
		    :cyan => "\033[0;36m",
		    :white => "\033[0;37m",
		    :b_black => "\033[1;30m",
		    :b_red => "\033[1;31m",
		    :b_green => "\033[1;32m",
		    :b_yellow => "\033[1;33m",
		    :b_blue => "\033[1;34m",
		    :b_violet => "\033[1;35m",
		    :b_cyan => "\033[1;36m",
		    :b_white => "\033[1;37m",
    	}
		colors[color] + text + colors[:normal]
	end
	
	def Terminal::move_cursor(direction, amount = 1)
		directions = {
			:up => "A",
			:down => "B",
			:right => "C",
			:left => "D",
		}
		print "\033[#{amount}#{directions[direction]}"
	end
	
	def Terminal::set_cursor(line, column)
		print "\033[#{line};#{column}H"
	end
	
	def Terminal::save_cursor
		print "\033[s"
	end
	
	def Terminal::restore_cursor
		print "\033[u"
	end

	def Terminal::input(prompt = "")
		print prompt + " "
		gets.chomp
	end
	
	def Terminal::input_password(prompt = "")
		begin
			system("stty -echo")
			password = input prompt
		ensure
			system("stty echo")
		end
		return password
	end
end

Terminal.read_password "Senha:"
