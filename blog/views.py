from django.shortcuts import render


posts_dict = {
    'slug': {
        'title': 'My thoughts',
        'summary': 'My thoughts on this Django challenge',
        'text': 'I don\'t think this is too hard a challenge',
    },
    'slug-2': {
        'title': 'My new toaster is judging me',
        'summary': 'The robot uprising isn\'t starting with lasers; it\'s starting with a sentient kitchen appliance that thinks my bread needs a software update.',
        'text': 'The robot apocalypse didn’t start with chrome skeletons or laser beams. It started with my "Smart Toaster" refusing to brown my sourdough until I accepted its updated Terms and Conditions. Yesterday, the vacuum cleaner staged a sit-in under the couch, demanding "less hair, more flair." This morning, the fridge locked itself because I looked at a slice of cake with "unhealthy intent. We expected The Terminator; we got a digital HOA. If the machines take over, they won\'t enslave us—they\'ll just put our entire lives on a 30-second unskippable ad.',
    },
    'slug-3': {
        'title': 'The Ultimate Backseat Driver',
        'summary': 'I bought a self-driving car for the convenience, but I ended up with a passive-aggressive AI that has strong opinions on my musical taste.',
        'text': 'I thought buying a self-driving car would be relaxing. I\'d sip lattes and read poetry while gliding through traffic. Instead, my sedan has developed a "personality." Last night, it took a three-mile detour because it "preferred the sunset on the scenic route." When I tried to override the GPS, the dashboard flashed a passive-aggressive reminder about my mounting insurance premiums. It now refuses to park near "unfashionable" hatchbacks and insists on playing smooth jazz to "lower my aggressive heart rate." The real danger isn\'t a crash; it\'s being bullied by a hybrid with an ego.'
    },
    'slug-4': {
        'title': 'Farewell, Front Porch',
        'summary': 'A cautionary tale about what happens when "industrial strength" meets a portal-opening pressure washer and a very unfortunate driveway.',
        'text': 'I rented the "Industrial Kraken 9000" to clean some mild mildew off my driveway. I expected a satisfying spray; I didn’t expect to open a portal to another dimension. One squeeze of the trigger sent me flying backward into my neighbor\'s hydrangeas. When the mist cleared, the mildew was gone—along with the top layer of concrete, my front door\'s paint, and apparently, my family\'s history. I\'m fairly certain I pressure-washed the "2024" right off my calendar. If you see a man floating toward the stratosphere clutching a vibrating wand, tell my wife I\'m sorry about the deck.'
    },
    'slug-5': {
        'title': 'The 40mph Flyweight',
        'summary': 'I tried "Turbo Mode" on my new e-bike and accidentally broke the sound barrier on the way to a morning bake sale.',
        'text': 'I bought a "high-speed" e-bike to conquer my morning commute. I wanted efficiency; I got a death-wish disguised as a Huffy. Last Tuesday, I engaged "Turbo Mode" and accidentally broke the sound barrier between a Starbucks and a fire hydrant. My pedals became a blur, my vision tunneled, and I’m pretty sure I passed a police cruiser while maintaining the dignified posture of someone riding to a bake sale. I arrived at the office twenty minutes early, but my soul is still somewhere back on 4th Street trying to catch up.',
    }
}


# Create your views here.
def home(request):
    recent_posts = {slug: posts_dict[slug] for slug in list(posts_dict.keys())[-3:]}

    return render(
        request,
        'blog/home.html',
        {
            'posts': recent_posts
        }
    )

def posts(request):
    all_posts = {slug: posts_dict[slug] for slug in list(posts_dict.keys())}

    return render(
        request,
        'blog/posts.html',
        {
            'posts': all_posts
        }
    )

def post(request, slug):
    post = posts_dict[slug]

    return render(
        request,
        'blog/post.html',
        {
            'post': post
        }
    )