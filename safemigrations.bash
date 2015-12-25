# This automation creates a fixture from the default database
# and writes it to a timestamped file in the ./recovery_fixtures
# directory.  Passing '-m' option also runs the django makemigrations
# command.

# By default does not run makemigrations command
makemigrations="False"
# Default outfile suffix is 'fixture'
outfile="fixture"

# If '-m' option is passed, set makemigrations to "True"
while getopts ":mo:" o; do
	case "${o}" in
		m)
			makemigrations="True"
			;;
		o)
			outfile=${OPTARG}
			;;
	esac
done
shift $((OPTIND-1))

# Calculate timestamp for the fixture file name
timestamp="$(date +"%Y-%m-%d_%H-%M-%S")"

# Make the fixture
echo "Making fixture:  ./recovery_fixtures/${timestamp}_${outfile}.json"
python3 manage.py dumpdata --output \
	./recovery_fixtures/${timestamp}_${outfile}.json \
	--natural-foreign --natural-primary -e contenttypes -e auth.Permission
	
# Conditionally run makemigrations
if [ ${makemigrations} == "True" ]; then
	echo "Running makemigrations:"
	python3 manage.py makemigrations
fi