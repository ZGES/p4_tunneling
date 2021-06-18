from apptopo import AppTopo

class CustomAppTopo(AppTopo):

    def __init__(self, *args, **kwargs):
        # Initialize the top topo
        AppTopo.__init__(self, *args, **kwargs)

        manifest, target = kwargs['manifest'], kwargs['target']

        print "Using target:", manifest['targets'][target]
        
        # Add hosts and switches
        Host1 = self.addHost( 'h1', ip='10.0.0.1/24', mac='00:00:00:00:00:01' )
        Host2 = self.addHost( 'h2', ip='20.0.0.1/24', mac='00:00:00:00:00:02'  )
        Host3 = self.addHost( 'h3', ip='30.0.0.1/24', mac='00:00:00:00:00:03'  )
        Switch1 = self.addSwitch('s1')
        Switch2 = self.addSwitch('s2')

        # Add links
        self.addLink( Host1, Switch1 )
        self.addLink( Host2, Switch1 )
        self.addLink( Host3, Switch2 )
        self.addLink( Switch1, Switch2 )
