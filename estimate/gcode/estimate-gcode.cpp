#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

int main(int argc, char **argv)
{
	int ret = 0;
	for(auto i = &argv[1]; i != &argv[argc]; ++i)
	{
		std::ifstream in(*i);
		if(!in)
		{
			ret = 1;
			continue;
		}

		double feedrate = 1.0;
		double x = 0.0;
		double y = 0.0;
		double z = 0.0;

		double time = 0.0;

		for(std::string s; getline(in, s);)
		{
			if(s.empty())
				continue;

			std::istringstream is(s);

			char c;
			if(!(is >> c))
				continue;

			if(c != 'G')
				continue;

			int n;
			if(!(is >> n))
			{
				ret = 1;
				continue;
			}

			if(n != 0 && n != 1)
				continue;

			double dist = 0.0;

			while(is)
			{
				if(!(is >> c))
					break;

				double d;
				if(!(is >> d))
					break;

				if(c == 'F')
					feedrate = d;
				else if(c == 'X')
				{
					dist = std::max(dist, std::abs(x - d));
					x = d;
				}
				else if(c == 'Y')
				{
					dist = std::max(dist, std::abs(y = d));
					y = d;
				}
				else if(c == 'Z')
				{
					dist = std::max(dist, std::abs(z - d));
					z = d;
				}
			}

			time += dist / feedrate;
		}

		std::cout << *i << " " << time << std::endl;
	}

	return ret;
}
