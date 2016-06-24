#include "json_cst.hpp"
#include "json_parse.hpp"
#include "json_lex.hpp"

#include <iostream>

std::string unquote(std::string const &s)
{
	if(s.size() < 2)
		return s;

	if(s[0] == '"' && s[s.size()-1] == '"')
		return s.substr(1, s.size() - 2);

	return s;
}

class dump_text :
	public taskserver::cst::node_const_visitor
{
public:
        virtual void visit(taskserver::cst::false_value const &) { std::cout << "false"; };
        virtual void visit(taskserver::cst::true_value const &) { std::cout << "true"; };
        virtual void visit(taskserver::cst::null_value const &) { std::cout << "null"; };
        virtual void visit(taskserver::cst::object_value const &o) { descend(o._1); }
        virtual void visit(taskserver::cst::array_value const &) { throw; }
        virtual void visit(taskserver::cst::number_value const &n) { std::cout << n._1; }
        virtual void visit(taskserver::cst::string_value const &s) { std::cout << s._1; }
        virtual void visit(taskserver::cst::object_3_chain const &c) { descend(c._1); descend(c._2); }
        virtual void visit(taskserver::cst::end_of_object_3 const &) { }
        virtual void visit(taskserver::cst::array_3_chain const &c) { descend(c._1); descend(c._2); }
        virtual void visit(taskserver::cst::end_of_array_3 const &) { }
        virtual void visit(taskserver::cst::json const &j) { descend(j._1); }
        virtual void visit(taskserver::cst::object const &o) { descend(o._1); descend(o._2); }
        virtual void visit(taskserver::cst::member const &m) { std::cout << unquote(m._1) << "="; descend(m._2); std::cout << std::endl; }
        virtual void visit(taskserver::cst::array const &a) { throw; }
        virtual void visit(taskserver::cst::object_3_elem const &e) { descend(e._1); }
        virtual void visit(taskserver::cst::array_3_elem const &) { throw; }
};

int main(int, char **)
{
	using namespace taskserver::cst;
	json_ptr job;
	{
		yyscan_t scanner;
		json_lex_init(&scanner);
		FILE *job_file = fopen("jobs.json", "r");
		if(job_file)
		{
			json_restart(job_file, scanner);
			json *tmp = nullptr;
			json_parse(scanner, tmp);
			job.reset(tmp);
			fclose(job_file);
		}
		json_lex_destroy(scanner);
	}

	dump_text dump;
	dump.visit(*job);

	return 0;
}
