# Generated by Django 4.2.2 on 2023-07-12 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), (None, 'Prefer not to Say')], default=None, max_length=1, null=True)),
                ('mlb', models.CharField(blank=True, choices=[('None', '--------------------'), ('ARI', 'Arizona Diamondbacks'), ('ATL', 'Atlanta Braves'), ('BAL', 'Baltimore Orioles'), ('BOS', 'Boston Red Sox'), ('CWS', 'Chicago White Sox'), ('CHC', 'Chicago Cubs'), ('CIN', 'Cincinnati Reds'), ('CLE', 'Cleveland Guardians'), ('COL', 'Colorado Rockies'), ('DET', 'Detroit Tigers'), ('HOU', 'Houston Astros'), ('KCR', 'Kansas City Royals'), ('LAA', 'Los Angeles Angels'), ('LAD', 'Los Angeles Dodgers'), ('MIA', 'Miami Marlins'), ('MIL', 'Milwaukee Brewers'), ('MIN', 'Minnesota Twins'), ('NYM', 'New York Mets'), ('NYY', 'New York Yankees'), ('OAK', 'Oakland Athletics'), ('PHI', 'Philadelphia Phillies'), ('PIT', 'Pittsburgh Pirates'), ('SD', 'San Diego Padres'), ('SF', 'San Francisco Giants'), ('SEA', 'Seattle Mariners'), ('STL', 'St. Louis Cardinals'), ('TB', 'Tampa Bay Rays'), ('TEX', 'Texas Rangers'), ('TOR', 'Toronto Blue Jays'), ('WAS', 'Washington Nationals')], default=None, max_length=20, null=True)),
                ('nfl', models.CharField(blank=True, choices=[('None', '--------------------'), ('ARI', 'Arizona Cardinals'), ('ATL', 'Atlanta Falcons'), ('BAL', 'Baltimore Ravens'), ('BUF', 'Buffalo Bills'), ('CAR', 'Carolina Panthers'), ('CHI', 'Chicago Panthers'), ('CIN', 'Cincinnati Bengals'), ('CLE', 'Cleveland Browns'), ('DAL', 'Dallas Cowboys'), ('DEN', 'Denver Broncos'), ('DET', 'Detroit Lions'), ('GB', 'Green Bay Packers'), ('HOU', 'Houston Texans'), ('IND', 'Indianapolis Colts'), ('JAX', 'Jacksonville Jaguars'), ('KC', 'Kansas City Chiefs'), ('MIA', 'Miami Dolphins'), ('MIN', 'Minnesota Vikings'), ('NE', 'New England Patriots'), ('NO', 'New Orleans Saints'), ('NYG', 'New York Giants'), ('NYJ', 'New York Jets'), ('LV', 'Las Vegas Raiders'), ('PHI', 'Philadelphia Eagles'), ('PIT', 'Pittsburgh Steelers'), ('LAC', 'Los Angeles Chargers'), ('SF', 'San Francisco 49rs'), ('SEA', 'Seattle Seahawks'), ('LAR', 'Los Angeles Rams'), ('TB', 'Tampa Bay Buccaneers'), ('TEN', 'Tennessee Titans'), ('WAS', 'Washington Commanders')], default=None, max_length=20, null=True)),
                ('nhl', models.CharField(blank=True, choices=[('None', '--------------------'), ('ANA', 'Anaheim Ducks'), ('ARI', 'Arizona Coyotes'), ('BOS', 'Boston Bruins'), ('BUF', 'Buffalo Sabres'), ('CAL', 'Calgary Flames'), ('CAR', 'Carolina Hurricanes'), ('CHI', 'Chicago Blackhawks'), ('COL', 'Colorado Avalanche'), ('CBJ', 'Columbus Blue Jackets'), ('DAL', 'Dallas Stars'), ('DET', 'Detroit Red Wings'), ('EDM', 'Edmonton Oilers'), ('FLA', 'Florida Panthers'), ('LAK', 'Los Angeles Kings'), ('MIN', 'Minnesota Wild'), ('MTL', 'Montreal Canadiens'), ('NSH', 'Nashville Predators'), ('NJD', 'New Jersey Devils'), ('NYI', 'New York Islanders'), ('NYR', 'New York Rangers'), ('OTT', 'Ottawa Senators'), ('PHI', 'Philadelphia Flyers'), ('PIT', 'Pittsburgh Penguins'), ('SJS', 'San Jose Sharks'), ('SEA', 'Seattle Kraken'), ('STL', 'St. Louis Blues'), ('TBL', 'Tampa Bay Lightning'), ('TOR', 'Toronto Maple Leafs'), ('VAN', 'Vancouver Canucks'), ('VGK', 'Vegas Golden Knights'), ('WAS', 'Washington Capitals'), ('WPG', 'Winnipeg Jets')], default=None, max_length=20, null=True)),
                ('nba', models.CharField(blank=True, choices=[('None', '--------------------'), ('ATL', 'Atlanta Hawks'), ('BOS', 'Boston Celtics'), ('CHA', 'Charlotte Hornets'), ('CHI', 'Chicago Bulls'), ('CLE', 'Cleveland Cavaliers'), ('DAL', 'Dallas Mavericks'), ('DEN', 'Denver Nuggets'), ('DET', 'Detroit Pistons'), ('GSW', 'Golden State Warriors'), ('HOU', 'Houston Rockets'), ('IND', 'Indiana Pacers'), ('LAC', 'Los Angeles Clippers'), ('LAL', 'Los Angeles Lakers'), ('MEM', 'Memphis Grizzlies'), ('MIA', 'Miami Heat'), ('MIL', 'Milwaukee Bucks'), ('MIN', 'Minnesota Timberwolves'), ('NOH', 'New Orleans Pelicans'), ('NYK', 'New York Knicks'), ('BKN', 'Brooklyn Nets'), ('OKC', 'Oklahoma City Thunder'), ('ORL', 'Orlando Magic'), ('PHI', 'Philadelphia 76ers'), ('PHO', 'Phoenix Suns'), ('POR', 'Portland Trail Blazers'), ('SAC', 'Sacramento Kings'), ('TOR', 'Toronto Raptors'), ('UTH', 'Utah Jazz'), ('WAS', 'Washington Wizards')], default=None, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
