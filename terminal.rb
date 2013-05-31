module Terminal

	def colorize(text, color)
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
	
	def move_cursor(direction, amount = 1)
		directions = {
			:up => "A",
			:down => "B",
			:right => "C",
			:left => "D",
		}
		print "\033[#{amount}#{directions[direction]}"
	end
	
	def set_cursor(line, column)
		print "\033[#{line};#{column}H"
	end
	
	def save_cursor
		print "\033[s"
	end
	
	def restore_cursor
		print "\033[u"
	end

	def input(prompt = "")
		print prompt + " "
		str = ""
	begin
	    system("stty raw")
    	system("stty -echo")
	    char = 0
	    esperando1 = false
	    esperando2 = false
	    numero = 0
	    index = 0
	    while (char != 13) do
            char = STDIN.getc
            if esperando1 == false
                if char == 27
                    esperando1 = true
                elsif char == 127 # Backspace
                    if index > 0
                        move_cursor :left
                        print " "
                        move_cursor :left
                        numero -= 1
                        index -= 1
                    end
                else
                    print char.chr
                    numero += 1
                    index += 1
                end
            else
                if char == 91
                    esperando2 = true
                elsif esperando2 == true
                    esperando2 = false
                    if char == 65 # Up
                        print "up"
                    elsif char == 66 # Down
                        print "down"
                    elsif char == 67 # Right
                        index += 1
                        if index <= numero
                            move_cursor :right
                        else
                            index -= 1
                        end
                    elsif char == 68 # Left
                        index -= 1
                        if index >= 0
                            move_cursor :left
                        else
                            index += 1
                        end
                    elsif char == 126 # Delete (TODO)
                        print ""                        
                    end
                    esperando1 = false
                end
            end
            str << char.chr
	    end
	ensure
    	system("stty -raw")
		system("stty echo")
    	print "\n"
	end
    	return str
	end
	
	def input_password(prompt = "")
		begin
			system("stty -echo")
			password = input prompt
			print "\n"
		ensure
			system("stty echo")
		end
		puts
		return password
	end
end
