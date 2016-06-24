#include "json_cst.hpp"
#include "json_parse.hpp"
#include "json_lex.hpp"

int main(int, char **)
{
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
	return 0;
}
