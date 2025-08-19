class WorkoutPlan:
    def init(self, plan_name, exercises):
        self.plan_name = plan_name
        self.exercises = exercises

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def remove_exercise(self, exercise):
        if exercise in self.exercises:
            self.exercises.remove(exercise)
        else:
            print(f'{exercise} is not in the plan')

    def view_plan(self):
        print(f'Workout Plan: {self.plan_name}')
        print('Exercises:')
        for exercise in self.exercises:
            print(f'- {exercise}')

class WorkoutTracker:
    def init(self):
        self.users_plans = {}

    def add_user_plan(self, username, workout_plan):
        self.users_plans[username] = workout_plan

    def get_user_plan(self, username):
        return self.users_plans.get(username)

    def track_progress(self, username, exercise, progress):
        user_plan = self.users_plans.get(username)
        if user_plan:
            if exercise in user_plan.exercises:
                print(f'Tracking progress for {exercise} for {username}: {progress}')
            else:
                print(f'{username} doesn\'t have {exercise} in their plan')
        else:
            print(f'No workout plan found for {username}.')

class HealthAdvisor:
    @staticmethod
    def give_tips():
        tips = [
            'Eat a healthy and balanced diet including fruits, vegetables, and proteins.',
            'Exercise regularly for at least 30 minutes per day.',
            'Ensure to get 7-8 hours of sleep each night and do not drink caffeinated beverages before going to sleep; the last one should be 3 hours before sleeping.',
            'Avoid smoking and excessive alcohol, maintain normal cholesterol and blood pressure levels.',
            'Stay hydrated by drinking an adequate amount of water.',
            'Limit intake of sugars, processed foods, and unhealthy fats.',
            'Manage stress and practice relaxation techniques like yoga or meditation.',
            'Take care of mental health by enjoying leisure time and pursuing favorite hobbies.'
        ]
        print('Some tips for a healthy lifestyle:')
        for tip in tips:
            print(f'- {tip}')

class GoalTracker:
    def init(self):
        self.health_goals = {}

    def set_goal(self, username, goal):
        self.health_goals[username] = goal

    def get_goal(self, username):
        return self.health_goals.get(username)

class UserProfile:
    def init(self, username):
        self.username = username
        self.daily_schedule = {}

    def add_schedule(self, time, activity):
        self.daily_schedule[time] = activity

    def get_schedule(self):
        return self.daily_schedule

    def send_notification(self, time, activity):
        print(f'Notification for {self.username}: Time to {activity} at {time}.')

    def update_progress(self, activity, progress):
        self.progress[activity] = progress

    def share_progress(self):
        if not self.progress:
            print("No progress to share yet.")
            return
        print(f"Progress update for {self.username}:")
        for activity, progress in self.progress.items():
            print(f"- {activity}: {progress}")

# Create workout plans
plan1 = WorkoutPlan('Beginner Plan', ['Push-ups', 'Squats', 'Cardio exercises'])
plan2 = WorkoutPlan('Intermediate Plan', ['Pull-ups', 'Deadlifts', 'Burpees'])
plan3 = WorkoutPlan('Professional Plan', ['Cardio exercises', 'Lunges', 'Plank'])

# Create a workout tracker and add user plans
tracker = WorkoutTracker()
tracker.add_user_plan('user1', plan1)
tracker.add_user_plan('user2', plan2)

# Get and view user plans
user_plan = tracker.get_user_plan('user1')
if user_plan:
    user_plan.view_plan()

# Track progress for users
tracker.track_progress('user1', 'Push-ups', '3 sets of 10 reps')
tracker.track_progress('user2', 'Squats', '4 sets of 12 reps')
tracker.track_progress('user1', 'Deadlifts', '5 sets of 8 reps')

# HealthAdvisor tips
HealthAdvisor.give_tips()

# GoalTracker set and get goals
goal_tracker = GoalTracker()
goal_tracker.set_goal('user1', 'Exercise for 30 minutes daily')
goal_tracker.set_goal('user2', 'Drink 8 glasses of water daily')
print(goal_tracker.get_goal('user1'))
print(goal_tracker.get_goal('user2'))

# Create user profiles
user1_profile = UserProfile('user1')
user1_profile.add_schedule('08:00 AM', 'Exercise')
user1_profile.add_schedule('12:00 PM', 'Lunch')
user1_profile.add_schedule('03:00 PM', 'Meeting')

# Send notifications based on user schedule
schedule = user1_profile.get_schedule()
for time, activity in schedule.items():
    user1_profile.send_notification(time, activity)

# Update and share progress
user1_profile.update_progress('Exercise', 'Completed 30 minutes of cardio.')
user1_profile.update_progress('Coding', 'Completed a new coding project.')
user1_profile.share_progress()