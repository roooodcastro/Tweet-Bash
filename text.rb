require "rubygems"
require "utils"
require "inifile"
	
module PrintText

	include Utils
	
	def translate(key_name, params={})
		get_language
		@strings ||= IniFile.new("lang/#{$language}.lang")
		text = @strings[key_name.split('.')[0]][key_name.split('.')[1]]
		process_text!(text, params) unless params.empty?
		return text unless text.nil?
		return ""
	end
	
	alias :t :translate
	
	private
	
	def process_text!(text, params)
		while text =~ /%{(.*)}/
#			text.substituir $1 pelos parametros, se $1 = param[0]
		end
	end
end
